#!/usr/bin/python

import sys

def getFirstSad(pancakes):
    for i, p in enumerate(pancakes):
        if p is '-':
            return i
    return None

def inverse(p):
    if p=='-':
        return '+'
    return '-'

def flipAt(pancakes, s, k):
    o = ""
    for i, p in enumerate(pancakes):
        if s <= i and i < s+k:
            o += inverse(p)
        else:
            o += p
    return o

def solvePancakes(pancakes, k):
    #print(pancakes, k, getFirstSad(pancakes))
    count = 0
    while True:
        s = getFirstSad(pancakes)
        if s is None:
            break
        if s+k > len(pancakes):
            return None
        pancakes = flipAt(pancakes, s, k)
        #print "\t%s" % pancakes
        count += 1
        #if count > 20:
        #    return -20
    return count

def main():
    f = open("input.txt")
    numTests = int(f.readline())
    output = ""
    for i in range(numTests):
        [pancakes, k] = f.readline().split(' ')
        k = int(k)

        answer = solvePancakes(pancakes, k)
        if answer != None:
            output += "Case #" + str(i+1) + ": " + str(answer) + '\n'
        else:
            output += "Case #" + str(i+1) + ": IMPOSSIBLE\n"

    fout = open("output.txt", "w")
    fout.write(output)

if __name__ == "__main__":
    main()

