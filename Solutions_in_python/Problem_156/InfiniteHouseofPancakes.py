#-------------------------------------------------------------------------------
# Name:        Infinite House of Pancakes
# Purpose:      GCJ 2015
#
# Author:      makwa python3
#
# Created:     11/04/2015
# Copyright:   (c) udonko 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
import math


debug = False
problemname="Infinite House of Pancakes"
def resolve(num_pancakes):


    def recursive(op):
        global debug
        num_pancakes.sort(reverse=True)
        maxnum = num_pancakes[0]

        if debug:
            print("val={0} list={1}".format(maxnum + op  ,str(num_pancakes)))
        if maxnum <= 3:
            return maxnum + op
        donothing = maxnum + op
        val = num_pancakes[0]//2
        val2 = num_pancakes[0] - val
        index = 0
        while True:
            if num_pancakes[index] == maxnum:
                num_pancakes[index] = val
                num_pancakes.append(val2)
                index += 1
            else:
                break
        ret = recursive(op+index)
        #ret = recursive(op+1)
        return min(ret, donothing)
    return recursive(0)
def resolve2(num_pancakes):
    num_pancakes.sort(reverse=True)
    maxnum = num_pancakes[0]
    if maxnum <= 3:
        return maxnum
    rtmax = int(math.ceil( math.sqrt(maxnum)) )
    endloop = max(rtmax,3)
    def recursive(op):
        global debug
        num_pancakes.sort(reverse=True)
        maxnum = num_pancakes[0]

        if debug:
            print("val={0} list={1}".format(maxnum + op  ,str(num_pancakes)))
        if maxnum <= endloop:
            return maxnum + op
        donothing = maxnum + op
        val = rtmax
        val2 = num_pancakes[0] - val
        index = 0
        while True:
            if num_pancakes[index] == maxnum:
                num_pancakes[index] = val
                num_pancakes.append(val2)
                index += 1
            else:
                break
        ret = recursive(op+index)
        #ret = recursive(op+1)
        return min(ret, donothing)
    return recursive(0)

def resolve3(num_pancakes):
    num_pancakes.sort(reverse=True)
    maxnum = num_pancakes[0]
    if maxnum <= 3:
        return maxnum
    rtmax = int(( math.sqrt(maxnum)) )
    endloop = max(rtmax,3)
    def recursive(op):
        global debug
        num_pancakes.sort(reverse=True)
        maxnum = num_pancakes[0]

        if debug:
            print("val={0} list={1}".format(maxnum + op  ,str(num_pancakes)))
        if maxnum <= endloop:
            return maxnum + op
        donothing = maxnum + op
        val = rtmax
        val2 = num_pancakes[0] - val
        index = 0
        while True:
            if num_pancakes[index] == maxnum:
                num_pancakes[index] = val
                num_pancakes.append(val2)
                index += 1
            else:
                break
        ret = recursive(op+index)
        #ret = recursive(op+1)
        return min(ret, donothing)
    return recursive(0)

def readfile_writefile(filename):
    with open(filename, "r") as inputfile:
        with open(problemname+"_out.txt", "w") as outputfile:
            num = int(inputfile.readline())
            for i in range(num):
                line1 = inputfile.readline().strip()
                non_empty = int(line1)
                line2 = inputfile.readline().strip()
                num_pancakes = list(map(int, line2.split()))
                result = min( resolve(num_pancakes[:]), resolve2(num_pancakes[:]), resolve3(num_pancakes[:]))
                outtext = "Case #{0}: {1}\n".format(i+1, result)
                #print(line1)
                #print(line2)
                #print(outtext)
                outputfile.write(outtext)

def main():
    if True:
        readfile_writefile(sys.argv[1])
    else:
        def test(arg, func):
            print("function name is " +func.__name__)
            print(str(arg))
            result = func(arg)
            print("result={0}".format(result))

        def test_all(arg):
            print("")
            test(arg[:], resolve)
            test(arg[:], resolve2)
            test(arg[:], resolve3)
        testdata =[
            [1,1,9],[8,4,2],[24,15,4]
        ]
        for testcase in testdata:
            test_all(testcase)


if __name__ == '__main__':
    main()
