def CC(a,n):
    L = len(a)
    for x in xrange(L-n):
        t = a[x:x+n]
        if (allCons(t)):
            return False
    return True 

def allCons(t):
    for c in t:
        if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
            return False
    return True

def solve(inf):
    s, n = inf.readline().split()
    n = int(n)
    L = len(s)
    tsum = 0
    for x in xrange(L-n+1):
        t = s[x:x+n]
        if (allCons(t)):
            for i in xrange(L-1,x+n-2,-1):
                for j in xrange(0,x+1):
                    if (CC(s[j:x+n],n)):
                        tsum = tsum+1
    return str(tsum)

if __name__ == '__main__':
    f = open('/home/steven/workspace/Codejam/Ain','r')
    out = open('/home/steven/workspace/Codejam/Aout','w')
    cases = [int(x) for x in f.readline().split()][0]
    for i in range(cases):
        print i
        out.write('Case #'+str(i+1)+': '+solve(f)+'\n')
    f.close()
    out.close()
    