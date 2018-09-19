#import psyco
#psyco.full()

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]

  def clear(self):
      self.memoized = {}

def gcd(a,b):
    while b: a,b = b, a%b
    return a
    
def alloc(size, default = 0): return [default] * size
def alloc2(r, c, default = 0): return [alloc(c, default)] * r
def isset(a, bit): return ((a >> bit) & 1) > 0
def dig(c): return ord(c) - 48
def abs(x): return x if x>=0 else -x
def area(x1, y1, x2, y2, x3, y3): return abs((x3-x1)*(y2-y1) - (x2-x1)*(y3-y1))/2
     
def maxarg(f, args):
    max=-1
    for a in args:
        x = f(a)
        if x>max:
            best=a
            max=x
    return best
    
###########################
from decimal import *
def fconv(x, precision=100, base=Decimal(3)):
    ans=[]
    for _ in range(precision):
        x*=base
        i = int(x)
        ans.append( str(i) )
        x-=i
        if x==0: break
    return "0." + "".join(ans)

#ans=[]
@memoize
def choose(n, k):
    if k>n: return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - i)
        c = c / (i + 1)
    return c


def center(i,j,k):
    pts=[(r,c) for r in range(i,i+k) for c in range(j,j+k)]
    pts.remove((i,j))
    pts.remove((i+k-1,j))
    pts.remove((i,j+k-1))
    pts.remove((i+k-1,j+k-1))
    #print pts
    #for r,c in pts:  print r,c,m[r][c]
    mass = sum(m[r][c] for r,c in pts)
    row = sum(m[r][c]*r for r,c in pts) / mass
    col = sum(m[r][c]*c for r,c in pts) / mass
    #print "center",i,j,k,"->",row,col, float(k-1)/2
    return row==i+float(k-1)/2  and col==j+float(k-1)/2
    
def solve():
    global R,C,D,m
    print R,C,D,m
    
    k=min(R,C)
    while k>=3:
        print k
        for i in range(R-k+1):
            for j in range(C-k+1):
                if center(i,j,k):
                    print i,j,k
                    return str(k)
        k-=1
    return "IMPOSSIBLE"

from time import time
if __name__ == "__main__":
    def getInts(): return map(int, input.readline().rstrip('\n').split(' '))
    def getInt(): return int(input.readline())
    def getFloats(): return map(float, input.readline().rstrip('\n').split(' '))
    def getMatrix(rows): return [getInts() for _ in range(rows)]
    def getFloatMatrix(rows): return [getFloats() for _ in range(rows)]
    def getString(): return input.readline().rstrip('\n')
    def getMatrixChars(rows): return [list(getString()) for _ in range(rows)]
    input, output = open("in", "r"), open('output', 'w')
    start_time=time()
    for case in range(1, int(input.readline()) + 1):
        R,C,D = getInts()
        m=[]
        for i in range(R):
            line=map(float,list(input.readline().rstrip('\n')))
            m.append([D+l for l in line])
        #m.reverse()
        ans=solve()
        s="Case #%d: %s\n" % (case,  ans)
        print s
        output.write(s)

    print time()-start_time

print choose.memoized