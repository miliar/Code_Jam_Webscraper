#cake

import random
from datetime import datetime

def number_sequence(seed):
    indices = [i for i in range(0,26)]
    random.seed(seed)
    random.shuffle(indices)
    return indices
    #return [4,2,1,0,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

special = [4,2,1,0,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
t = int(input())
for i in range(1, t+1):
    dimensions = input().split()
    R = int(dimensions[0])
    C = int(dimensions[1])
    letters = [[-1,-1,-1,-1] for l in range(0,26)] #each letter has left, top, right and bottom of rectangle
    grid = []
    for r in range(0, R):
        row = list(input())
        for f in range(0,C):
            #print("f is {}".format(f))
            if row[f] != "?":
                let_index = alpha.index(row[f])
                letters[let_index] = [f,r,f,r]
        grid.append(row)    
    
    fresh_grid = grid
    fresh_letters = letters
    #print(letters)
    
    solution_found = False
    starting_letter = 0
    current_list = []
    while not solution_found:
        grid = fresh_grid
        letters = fresh_letters
        #expand each letter's rectangle until grid is filled
        current_list = number_sequence(starting_letter)
        #print(current_list)
        m = 0
        for m in range(0,26):
            c = current_list[m]
            #c = (m+starting_letter)%26
            #c = special[m]
            #print("start {}".format(starting_letter))
            #print("m {}".format(m))
            #print("c {}".format(c))
            if letters[c][0] == -1:
                continue
            #expand right
            while True:
                if letters[c][2] + 1 >= C:
                    break
                available_to_place = True
                h = 0
                for h in range(0, letters[c][3] - letters[c][1] + 1):
                    #print("row")
                    #print(letters[c][1]+h)
                    #print("column")
                    #print(letters[c][2]+1)
                    if grid[letters[c][1]+h][letters[c][2]+1] != "?":
                        available_to_place = False
                        break
                if available_to_place:
                    y = 0
                    for y in range(0, letters[c][3] - letters[c][1] + 1):
                        grid[letters[c][1]+y][letters[c][2]+1] = alpha[c]
                    letters[c][2] += 1
                else:
                    break
            #expand left
            while True:
                if letters[c][0] - 1 <= -1:
                    break            
                available_to_place = True
                h = 0
                for h in range(0, letters[c][3] - letters[c][1] + 1):
                    #print("row")
                    #print(letters[c][1]+h)
                    #print("column")
                    #print(letters[c][2]+1)
                    if grid[letters[c][1]+h][letters[c][0]-1] != "?":
                        available_to_place = False
                        break
                if available_to_place:
                    y = 0
                    for y in range(0, letters[c][3] - letters[c][1] + 1):
                        grid[letters[c][1]+y][letters[c][0]-1] = alpha[c]
                    letters[c][0] -= 1
                else:
                    break
            #expand down
            while True:
                if letters[c][3] + 1 >= R:
                    break            
                available_to_place = True
                h = 0
                for h in range(0, letters[c][2] - letters[c][0] + 1):
                    #print("row")
                    #print(letters[c][1]+h)
                    #print("column")
                    #print(letters[c][2]+1)
                    if grid[letters[c][3]+1][letters[c][0]+h] != "?":
                        available_to_place = False
                        break
                if available_to_place:
                    y = 0
                    for y in range(0, letters[c][2] - letters[c][0] + 1):
                        grid[letters[c][3]+1][letters[c][0]+y] = alpha[c]
                    letters[c][3] += 1
                else:
                    break
            #expand up
            while True:
                if letters[c][1] -1 <= -1:
                    break            
                available_to_place = True
                h = 0
                for h in range(0, letters[c][2] - letters[c][0] + 1):
                    #print("row")
                    #print(letters[c][1]+h)
                    #print("column")
                    #print(letters[c][2]+1)
                    if grid[letters[c][1]-1][letters[c][0]+h] != "?":
                        available_to_place = False
                        break
                if available_to_place:
                    y = 0
                    for y in range(0, letters[c][2] - letters[c][0] + 1):
                        grid[letters[c][1]-1][letters[c][0]+y] = alpha[c]
                    letters[c][1] -= 1
                else:
                    break
        final = []
        g = 0
        for g in range(0,R):
            u = 0
            for u in range(0,C): 
                final.append(grid[g][u])
        #print(final)
        if not "?" in final:
            solution_found = True
            print("Case #{}:".format(i))
            line = 0
            for line in range(0,R):
                print("".join(grid[line]))
        else:
            print("here")
            starting_letter += 1
                    
        