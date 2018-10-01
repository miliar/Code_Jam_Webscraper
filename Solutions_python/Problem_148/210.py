from sys import argv
import math
import linecache

filename = argv[1]

with open(filename, 'r') as data:
    num = int(data.readline())

    for case in xrange(1, num+1):
        stored, capacity = [int(i) for i in data.readline().split()]
        xs = [int(i) for i in data.readline().split()]
        xs.sort()
        needed = 0

        while(len(xs) > 0):
            needed += 1
            m = xs.pop()
            i = len(xs)-1

            while(i >= 0):
                if(m + xs[i] <= capacity):
                    del xs[i]
                    break
                else:
                    i -= 1

        print "Case #%i: %i" % (case, needed)

