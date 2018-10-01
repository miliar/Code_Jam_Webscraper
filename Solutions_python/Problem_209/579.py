
import sys
import heapq
from math import pi

def pancakes2(input_file, output_file):
    T = int(input_file.readline())

    for case in xrange(1, T + 1):
        args = input_file.readline().split(' ')
        N = int(args[0])
        K = int(args[1])
        maxR = 0
        surfaces = [0]*N
        circle = [0]*N
        sides = [0]*N
        totals = [0]*N

        for index in range(N):
            args = input_file.readline().split(' ')
            R = int(args[0])
            H = int(args[1])
            circle[index] = pi * R * R
            sides[index] = 2 * pi * R * H
            surfaces[index] = circle[index] + sides[index]

        circle, sides, surfaces = zip(*sorted(zip(circle, sides, surfaces), reverse=True))
        for index in range(N - K + 1):
            totals[index] = surfaces[index] + sum(heapq.nlargest(K-1, sides[index + 1:]))

        total_surface = max(totals)

        output_file.write("Case #" + str(case) + ": " + str(total_surface) + "\n")

#pancakes2(sys.stdin, sys.stdout)

input_file = open("C:\\Users\\doritm\\Desktop\\A-small.in", "r")
output_file = open("C:\\Users\\doritm\\Desktop\\output.out", "w")
pancakes2(input_file, output_file)
input_file.close()
output_file.close()

