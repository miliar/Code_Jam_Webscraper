import sys

m = 0
sums = set()


def calcSum(ar):
    a = 0
    for a1 in ar:
        a = a ^ a1
    return a


def main():
    global ar1, m1, m2, m
    infile = open('C-large.in', 'r');
    cases = int(infile.readline());
    f = open('C-large.out', 'w')

    
    for case in range(1, cases+1):
        ans = 0
        line = infile.readline().strip().split();
        
        N = int(line[0])
        
        line = infile.readline().strip().split();
        
        C = []
        for c in range(N):
            C.append(int(line[c]))
        C.sort()
        
        if calcSum(C) == 0:
            ans = sum(C[1:])
        else:
            ans = 0
        
        if ans == 0:
            ans = 'NO'
        s = "Case #%d: %s\n" % (case, ans)
        print s,
        f.write(s)
    
    f.close()
main();