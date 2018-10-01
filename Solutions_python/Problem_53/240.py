import sys


cases=int(sys.stdin.readline())

for i in range(1, cases+1):
    [n, k]=sys.stdin.readline().split()
    n=int(n)
    k=int(k)
    if (k%(2**n) == 2**n -1):
        print "Case #%d: ON"%i
    else:
        print "Case #%d: OFF"%i
