import re
from sys import argv
zrl = lambda xs: zip(range(len(xs)), xs)

def snapper(k, n):
    mask = (1 << n) - 1
    state = k & mask
    testmask = 1 << n
    test = (state + 1) & testmask
    return bool(test)

def offon(the_bool):
    return ('OFF','ON')[int(the_bool)]

lines = open(argv[1], 'r').readlines()
linecount = int(re.search('''^\s*(\d+)\s*$''', lines[0]).group(1))

#print 'line count', linecount
for i, line in zrl(lines[1:linecount+1]):
    groups = re.search('''^\s*(\d+)\s*(\d+)\s*$''', line).groups()
    n, k = [int(x) for x in groups]
    print "Case #%d: %s" % (i+1, offon(snapper(k, n)))



