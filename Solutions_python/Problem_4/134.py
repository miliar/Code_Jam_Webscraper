#!/usr/bin/python
import sys

class Vector:
    def __init__(self, line):
        self.numbers = []
        for number in line.strip("\n").split(" "):
            self.numbers.append(int(number))
        self.numbers.sort()


def mulVectors(v1, v2):

	sum = 0
	while len(v1.numbers) > 0:
 	   sum = sum + v1.numbers.pop() * v2.numbers.pop(0)
 	return sum

infile = open(sys.argv[1])
outfile = sys.stdout
num_cases = int(infile.readline().strip("\n"))
i = 1
for i in range(num_cases):
        vectorLengths = int(infile.readline().strip("\n"))
        line1 = infile.readline()
        line2 = infile.readline()
        minScalProd = mulVectors(Vector(line1), Vector(line2))
        outfile.write(''.join(["Case #", str(i+1), ": ", str(minScalProd), "\n"]))
