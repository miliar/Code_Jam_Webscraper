#! /usr/bin/python
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

def select(queue, k, index=0):
    groups = len(queue)
    people = 0
    shift = 0
    for i in xrange(index, index+groups):
        i = i % groups
        if people + queue[i] > k:
            break
        people += queue[i]
##     print "%s(%d) -> %d (%d)" % (queue, index, people, i)
    return people, i

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines.pop(0))
    testcase = 0
    while testcase < T:
        testcase += 1
        R, k, N = map(int, lines.pop(0).split())
        queue = map(int, lines.pop(0).split())
##         print "R: %d, k: %d, N: %d, G: %s" % (R, k, N, queue)

        index = 0
        euros = 0
        for i in xrange(R):
            people, index = select(queue, k, index)
            euros += people
        print "Case #%d: %d" % (testcase, euros)
##     select([2, 4, 2, 3, 4, 2, 1, 2, 1, 3], 11, 9)

if __name__ == '__main__':
    main()
