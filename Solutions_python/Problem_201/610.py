import time
##import sys
##sys.setrecursionlimit(10002)
INFILE='cl.in'
OUTFILE='c.out'

def sp(n):
    n-=1
    return [n-n/2,n/2]
def solve1(n,c0,c1,k):
    a=sp(n)
    b=sp(n+1)
    if k<=c1:
        return b
    if k<=c0+c1:
        return a
    if a[0]==a[1]:
        return solve1(a[0],c0*2+c1,c1,k-c0-c1)
    else:
        return solve1(a[1],c0,c0+c1*2,k-c0-c1)

def solve(n,k):
    if k==n:
        return "0 0"
    return ' '.join(map(str,solve1(n,1,0,k)))

def read_input(fi):
    read=lambda type:type(fi.readline()[:-1])
    readArray=lambda type:map(type,fi.readline().split())
    readMatrix=lambda type,x:[map(type,fi.readline().split()) for i in range(x)]
    readLines=lambda type,x:[type(fi.readline()[:-1]) for i in range(x)]
    n,k=readArray(int)
    return n,k

def main():
    fi=file(INFILE)
    fo=file(OUTFILE,'w')
    time0=time.time()
    t=int(fi.readline())
    for ti in range(t):
        time1=time.time()
        ans="Case #%d: %s"%(ti+1,solve(*read_input(fi)))
        print ans,"%.3f"%(time.time()-time1)
        fo.write(ans+'\n')
    print "%.3f"%(time.time()-time0)
    fi.close()
    fo.close()

if __name__ == '__main__':
    main()
