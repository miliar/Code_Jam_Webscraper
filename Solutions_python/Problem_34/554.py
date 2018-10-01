# Python 2.5.4
# SMALL INPUT: program.py < A.small.in > A.small.out
# LARGE INPUT: program.py < A.large.in > A.large.out
import re

words = set()

def proc_case(num, pattern):
    r = re.compile(pattern)
    accepted = [w for w in words if r.match(w) != None]
    print "Case #%d: %d" % (num, len(accepted))

def main():
    m = re.search("(\d+)\s+(\d+)\s+(\d+)", raw_input()).groups()
    L = int(m[0])
    D = int(m[1])
    N = int(m[2])

    for i in xrange(0, D):    
        words.add(raw_input())

    for i in xrange(0, N):
        pattern = raw_input()
        pattern = pattern.replace('(', '[').replace(')', ']')
        proc_case(i + 1, pattern)

if __name__ == '__main__':
    main()

    
