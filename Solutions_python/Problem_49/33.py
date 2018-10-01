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
            case = DCase(input)
            result = case.solve()
            print ("Case #" + str(index + 1) + ": " + str(result))
            output.write("Case #" + str(index + 1) + ": " + str(result) + "\n")
class DCase:
    def __init__(self, file):
        self.n = int(input.readline())
        self.values = []
        for i in range(self.n):
            self.values.append([int(part) for part in file.readline().strip().split()])
    def solve(self):
        maximumRange = 0;
        for i in self.values:
            if (i[2] > maximumRange):
                maximumRange = i[2];
        if (self.n < 3):
            return str(maximumRange)
        toAdd = [self.getRange(self.values[0], self.values[1]), self.getRange(self.values[1], self.values[2]), self.getRange(self.values[0], self.values[2])]
        toAdd.sort();
        if (toAdd[0] > maximumRange):
            return str(toAdd[0]/2)  
        return str(maximumRange);
    def getRange(self, first, second):
        return math.sqrt(math.pow(first[0] - second[0], 2) + math.pow(first[1] - second[1], 2)) + first[2] + second[2];

class CCase:
    def __init__(self, file):
        self.n, self.k = [int(part) for part in file.readline().strip().split()]
        self.values = []
        for i in range(self.n):
            self.values.append([int(part) for part in file.readline().strip().split()])
    def solve(self):
        addables = []
        for values in self.values:
            addable = []
            for (i,valuesToCompare) in enumerate(self.values):
                if (self.match(values, valuesToCompare)):
                    addable.append(i)
            addables.append(addable)
        total = 1
        for (i, addable) in enumerate(addables):
            if (len(addable) == 0):
                total+=1
                addables.remove(addable)
                                     
        return str(len(addables) + total)
    def match(self, first, second):
        sign = False
        for (i, value) in enumerate(first):
            if (value == second[i]):
                return False
            if (i == 0):
                sign = value < first[i]
            else:
                if (sign != (value < first[i])):
                    return False
        return True
               
class BCase:
    def __init__(self, file):
        self.amountOfPoints = int(file.readline())
        self.points = []
        for i in range(self.amountOfPoints):
            self.points.append([int(part) for part in file.readline().strip().split()])
    def solve(self):
        current = [0,0,0,0,0,0]
        for i in self.points:
            for j in range(len(i)):
                current[j] = current[j] + i[j];
        for j in range(len(i)):
            current[j]/=self.amountOfPoints
        if ((current[3]*current[3] + current[4]*current[4] + current[5]*current[5] )> 0):
            t = -(2*current[0]*current[3] + 2*current[1]*current[4] + 2*current[2]*current[5])/(2*(current[3]*current[3] + current[4]*current[4] + current[5]*current[5]))
        else:
            t = 0;
        if (t < 0):
            t = 0;
        d = math.sqrt(math.pow(current[0]+current[3]*t, 2) + math.pow(current[1]+current[4]*t, 2) + math.pow(current[2]+current[5]*t, 2))
        return str(d) + " " + str(t);
class ACase:
    def __init__(self, file):
        amountOfLines= int(input.readline())
        self.values = [];
        for i in range(amountOfLines):
            self.values.append(input.readline().strip().rfind("1"))
    def solve(self):
        total = 0;   
        while (True):
            k = -1;
            toSwitchTo = -1;
            for (i, value) in enumerate(self.values):
                if i < value and (k == -1):
                    k = i;
                else:
                    if (k != -1 and value <= k):
                        toSwitchTo = i;
                        break;
            if (k == -1):
                break;
            self.values.insert(k, self.values[toSwitchTo])
            self.values.pop(toSwitchTo + 1)
            total += toSwitchTo - k
        return total;


        
                
                
        
type = "D"
if (1):
    size = "-small-attempt1" 
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

