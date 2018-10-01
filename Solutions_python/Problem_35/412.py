#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    
    #nacteni 2 cisel
    numbers = sys.stdin.readline()[:-1].split()
    height = int(numbers[0])
    width = int(numbers[1])

    # zde seznam seznamu
    list = []
    #nacitani cisel v radku do promenne
    for i in range(height):
        line = sys.stdin.readline()[:-1].split()
        line_list = []
        for j in range(width):
            line_list.append(int(line[j]))
        list.append(line_list)

    #print list

    free_number = 0

    big = 11000
    array = [[-1]*width for i in range(height)]
    for i in range(height):
        for j in range(width):
            if array[i][j] == -1:
                x = i
                y = j
                char = 'x'
                same = []
                while char != 'a' and array[x][y] == -1:
                    same.append((x,y))
                    act = list [x][y]   # letter a
                    if x == 0:
                        up = big        # letter b
                    else:
                        up = list[x-1][y]
                    if y == 0:
                        west = big      # letter c
                    else:
                        west = list[x][y-1]
                    if y == width-1:
                        east = big      # letter d
                    else:
                        east = list[x][y+1]
                    if x == height - 1:
                        down = big      # letter e
                    else:
                        down = list[x+1][y]
                    result_cell = min((act,'a',x,y),
                                      (up,'b',x-1,y),
                                      (west,'c',x,y-1),
                                      (east,'d',x,y+1),
                                      (down,'e',x+1,y))
                    (num,char,x,y) = result_cell
                if char == 'a':
                    array[x][y] = free_number
                    free_number += 1
                for (ii,jj) in same:
                    array[ii][jj] = array[x][y]

    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    free_alph = 0
    dic = dict()
    for i in range(height):
        for j in range(width):
            if array[i][j] not in dic.keys():
                dic[array[i][j]] = alphabeth[free_alph]
                free_alph += 1
            array[i][j] = dic[array[i][j]]
    
    print "Case #%d:" %(actual_case)
    
    for i in range(height):
        print ' '.join(array[i]) 
            
