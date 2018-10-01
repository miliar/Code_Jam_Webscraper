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


def solve():
    global x,s,r,t,n
    #print x,s,r,t,n
    #print walks
    segs=[ [w, e-b] for b,e,w in walks ]
    
    segs.append( [0, x - sum(s[1] for s in segs)] )
    
    segs.sort()#reverse=True)
    #print segs
    y=0
    i=0
    while i < len(segs):
        speed, dist = segs[i]
        #print i, y, segs[i], t
        if t>0:
            sp=r+speed
            if t > dist/sp:
                # run all of it!
                t-=dist/sp
                y+=dist/sp
                i+=1
            else:
                #run part!
                y+=t
                segs[i][1] -= sp*t
                t=0
        else:
            #just walk it
            sp=s+speed
            y+=dist/sp
            i+=1
    return y

from time import time
if __name__ == "__main__":
    def getInts(): return map(int, input.readline().rstrip('\n').split(' '))
    def getInt(): return int(input.readline())
    def getFloats(): return map(float, input.readline().rstrip('\n').split(' '))
    def getMatrix(rows): return [getInts() for _ in range(rows)]
    def getString(): return input.readline().rstrip('\n')
    def getMatrixChars(rows): return [list(getString()) for _ in range(rows)]
    input, output = open("in", "r"), open('output', 'w')
    start_time=time()
    for case in range(1, int(input.readline()) + 1):
        x,s,r,t,n = getFloats()
        walks = sorted([tuple(getFloats()) for i in range(int(n))])
        ans=solve()
        s="Case #%d: %f\n" % (case,  ans)
        print s
        output.write(s)

    print time()-start_time

print choose.memoized