import sys
import math
import decimal
import copy
import re


class Solver:
    def __init__(self, input, output):
        size = int(input.readline())
        print (str(size))
        for index in range(size):
            case = BCase(input)
            result = case.solve()
            print ("Case #" + str(index + 1) + ": " + str(result))
            output.write("Case #" + str(index + 1) + ": " + str(result) + "\n")
        
class BCase:
    def __init__(self, file):
        numbers = [int(part) for part in file.readline().strip().split()]
        self.height = numbers[0]
        self.width = numbers[1]
        self.fields = []
        for i in range(self.height):
            for j,k in enumerate([int(part) for part in file.readline().strip().split()]):
                neighbours = []
                if (i != 0):
                    neighbours.append(self.fields[(i-1) * self.width + j])
                if (j != 0):
                    neighbours.append(self.fields[len(self.fields)-1])
                self.fields.append(field(k, neighbours, i))
    def solve(self):
        result = "\n";
        line = 0
        self.fields[0].determineType("a")
        for field in self.fields:
            if (field.line > line):
                result = result + "\n"
                line = field.line
            type = field.determineType("b")
            result = result + type + " ";

        return result         
class field:
    def __init__(self, altitude, neighbours, line):
        self.altitude = altitude
        self.neighbours = neighbours
        self.line = line
        for neighbour in self.neighbours:
            neighbour.addNeighbour(self)
        self.type = None
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)        
    def determineType(self, possibleType):
        if (self.type != None):
            return self.type
        next = self.determineToFlowTo();
        if (next == None):
            self.type = possibleType;
        else:
            self.type = next.determineType(possibleType)
        return self.type
    def determineToFlowTo(self):
        result = None
        for neighbour in self.neighbours:
            if (neighbour.altitude < self.altitude and (result == None or neighbour.altitude < result.altitude)):
                result = neighbour
        return result
                
        
        
type = "B"
if (1):
    size = "-small-attempt3" 
else: 
    size = "-large"
filename = "..\\" + type + size + ".in"
outputname = "result.txt"
input = open(filename, 'r')
output = open(outputname, 'w')
try:
    Solver(input, output)
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
finally:
    input.close()
    output.close()

