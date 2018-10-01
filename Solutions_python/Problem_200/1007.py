

def Solver(num):

    s = str(num)

    marker = 0

    for idx in range(len(s)-1):

        c = int(s[idx])
        n = int(s[idx+1])

        if n>c:
            marker = idx+1

        if n<c:
            return s[:marker] + str(int(s[marker])-1) +'9'*(len(s)-marker-1)

    return s

import sys

def main():

    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in xrange(nums):
            n, = f.readline().strip().split()
            n = int(n)

            r = Solver(n)
            print "Case #{:d}: ".format(i+1)+str(int(r))

    #print Solver('---+-++-',3)
    #print Solver('+++++',4)
    #print Solver('-+-+-',4)

main()
