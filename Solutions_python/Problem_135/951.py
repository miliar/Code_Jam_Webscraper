import sys
import time


def solve_case(first_row, second_row):
    counter = 0
    answer = ""
    for element in first_row:
        if element in second_row:
            counter +=1
            answer = element

    if counter == 0:
        return "Volunteer cheated!"
    elif counter == 1:
        return answer
    else:
        return "Bad magician!"

f = open("A-small-attempt0.in")
fout = open("output.txt", "w")
T = int(f.readline().rstrip())

for ii in range(T):
    first_guess = int(f.readline().rstrip())
    grid_one = []
    for jj in range(4):
        line_list = f.readline().rstrip().split(" ")
        grid_one.append(line_list)

    second_guess = int(f.readline().rstrip())
    grid_two = []
    for jj in range(4):
        line_list = f.readline().rstrip().split(" ")
        grid_two.append(line_list)

    first_row = grid_one[first_guess - 1]
    second_row = grid_two[second_guess - 1]
    
    answer = solve_case(first_row, second_row)

    print "Case #"+str(ii+1)+": "+str(answer)
    fout.write("Case #"+str(ii+1)+": "+str(answer)+"\n")

fout.close()

