# Python 3.6.1

import math

def main():
    problem = open("A-large.in", "r")
    output = open("A-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        N = int(line[0])
        K = int(line[1])
        pancake_rad = []
        pancake_cylinder = []
        for i in range(N):
            line = problem.readline().strip().split()
            pancake_rad.append(int(line[0]))
            pancake_cylinder.append(2 * math.pi * int(line[0]) * int(line[1]))
        max_val = 0
        for i in range(N):
            selected = []
            for j in range(N):
                if i == j: continue
                if pancake_rad[i] >= pancake_rad[j]:
                    selected.append(pancake_cylinder[j])
            surface = math.pi * (pancake_rad[i] ** 2)
            surface += pancake_cylinder[i]
            surface += sum(sorted(selected, reverse=True)[:K-1])
            if max_val < surface:
                max_val = surface
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(max_val) + "\n")
    problem.close()
    output.close()

main()
