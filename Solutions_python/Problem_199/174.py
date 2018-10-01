from __future__ import print_function

def solveProblem(s, k):
    result = []
    pancakes = [x for x in s]
    flips = 0

    for i in xrange(len(pancakes)):
        if pancakes[i] == '+':
            continue
        else:
            #check to see if flippable
            if i + k > len(pancakes):
                result = ['IMPOSSIBLE']
                print(pancakes)
                return result
            else:
                for j in range(k):
                    if pancakes[i+j] == '-':
                        pancakes[i+j] = '+'
                    elif pancakes[i+j] == '+':
                        pancakes[i+j] = '-'
                flips += 1
    result = [flips]
    print(pancakes)



    return result

import sys

def main():
    inPath = sys.argv[1]
    outPath = inPath.split('.')[0] + '.out'
    file = open(inPath, "r")
    out = open(outPath, "w")
    case = 0
    #Read Input File
    for line in file:
        #Skip first line
        if case == 0:
            case += 1
            continue
        #solve problem
        inputs = line.split(' ')
        result = solveProblem(inputs[0], int(inputs[1]))
        #format Problem
        resultStr = ""
        for r in result:
            resultStr += str(r) + ' '
        print('Case #{case}: {resultStr}'.format(case=case, resultStr=resultStr), file=out)
        case += 1

if __name__ == "__main__":
    main()