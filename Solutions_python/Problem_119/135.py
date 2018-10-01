#!/usr/bin/python

import sys
import functools
import operator

def solve(akeys, achests):
    results = dict()

    def recSolve(keys, chests):
        if not chests:
            return ''
        if not keys:
            return 'IMPOSSIBLE'

        for chest in chests:
            if chest[1] in keys:
                newkeys = list(keys)
                newkeys.remove(chest[1])
                newkeys.extend(chest[2])
                newchests = list(chests)
                newchests.remove(chest)
                
                hashedkey = 'key' + str([newchest[0] for newchest in  newchests])
                if hashedkey in results:
                    r = results[hashedkey]
                else:
                    r = recSolve(newkeys, newchests)
                    results[hashedkey] = r

                if r != 'IMPOSSIBLE':
                    return str(chest[0]) + ' ' + r
        return 'IMPOSSIBLE'

    return recSolve(akeys, achests)

def main():
    N = int(sys.stdin.readline()) # number of testcases
    for i in range(N):
        [numkeys, numchests] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        keys = [int(x) for x in sys.stdin.readline().rstrip().split()]
        chests = []
        for j in range(numchests):
            line = [int(x) for x in sys.stdin.readline().rstrip().split()]
            chest = [j+1, line[0], line[2:]]
            chests += [chest]
        result = solve(keys, chests)
        print ("Case #%s: %s" % (i+1, result))


if __name__ == '__main__':
    main()
