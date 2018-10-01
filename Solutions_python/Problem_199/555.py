import sys

def solve(l, fsize):
    count = 0
    size = len(l)
    for i in xrange(size-fsize+1):
        if not l[i]: # Needs change
            #flip!
            count +=1
            for j in xrange(i, i+fsize):
                if l[j]:
                    l[j] = False
                else:
                    l[j] = True
    for i in xrange(size-fsize+1, size):
        if not l[i]:
            return "IMPOSSIBLE"
    return str(count)

def parse(s):
    l = []
    i = 0
    while s[i] != ' ':
        if s[i] == '-':
            l += [False]
        else:
            l += [True]
        i += 1
    fsize = int(s[i+1:])
    return solve(l, fsize)

def process(filenamein):
    f = open(filenamein, "r")
    size = int(f.readline())
    for line in xrange(size):
        s = f.readline()
        res = parse(s)
        out = "Case #" + str(line+1) + ": " + res
        print out
    f.close()

if len(sys.argv) == 2:
    process(sys.argv[1])