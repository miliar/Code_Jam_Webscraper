class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

@memoize
def choose(n, k):
    
    if k==0:
        return 1
    if n==0:
        return 0
    if n<k:
        #print "SDFSDF"
        return 0
    return (choose(n-1, k) + choose(n-1, k-1)) % 100003

#number of ways to pick s, subset of {2...n}, with rank(n)=size(s)=r
@memoize
def f(n, r):
    if r==1:
        x=1
    else:
        x=0
        for i in range(1, r): # i is where to put "r"
            x+= (f(r, i) * choose(n-r-1, r-i-1)) % 100003
            #print "x+= f(%d, %d) * choose(%d, %d) = "%(r,i,n-r-1, r-i-1), "%d * %d"%(f(r, i),choose(n-r-1, r-i-1))
    #print "f(%d,%d) = %d"% (n,r,x)
    return x %100003
    

        # s is of size 'size'
        # thus n is last, in position 'size'
        # we have g(size) options for the left part
        # we have choose(n-size
print "sdgf"
for n in range(2,500):
    #print n
    for r in range(1,n):
        f(n,r)
    
print "sdgf"   
input = open("e:/C-large.in", "r")
for testcase in range(1, int(input.readline())+1):
    N = int(input.readline())  
    print "Case #%d:"%testcase, sum(f(N, r) for r in range(1,N))%100003


