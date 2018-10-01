#<boilerplate>
def alloc(size, default = 0): return [default] * size
def alloc2d(r, c, default = 0): return [alloc(c, default)] * r

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
      if args not in self.memoized:
        self.memoized[args] = self.function(*args)
      return self.memoized[args]


from bisect import *
def binary_search(a, x, low=0):    
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x, low)
    if i != len(a) and a[i] == x:
        return i
    return None
#</boilerplate>

def solve(O, B, L):
    o,b = 1,1
    count=0
    while L!=[]:
        press=False
        if O!=[]: 
            if o==O[0]:
                if L[0]=='O' and o==O[0]:
                    #O press button
                    L=L[1:]
                    O=O[1:]
                    press=True
            elif o<O[0]:
                o+=1
            else:
                o-=1
        if B!=[]:    
            if b==B[0]:
                if not press and L[0]=='B' and b==B[0]:
                    #B press button
                    L=L[1:]
                    B=B[1:]
            elif b<B[0]:
                b+=1
            else:
                b-=1    
        
        count+=1
        #print o,b
        
    return count

from time import time
if __name__ == "__main__":
    def getInts():
        return map(int, data.readline().rstrip('\n').split(' '))
    start_time=time()
    output = open('d:/gcj/output', 'w')
    #data = open("d:/gcj/A-large.in", "r")
    data = open("d:/gcj/in.txt", "r")
    N = int(data.readline())
    for case in range(1, N + 1):
        line = data.readline().rstrip('\n').split(' ')
        C = int(line[0])
        i=1
        O=[]
        B=[]
        L=[]
        for _ in range(C):
            t = line[i]
            L.append(t)
            x = int(line[i+1])
            if t=='O':
                O.append(x)
            else:
                B.append(x)
            i+=2    
        ans = solve(O,B,L)
        s = "Case #%d: %d\n"%(case, ans)
        print s,
        output.write(s)
    print "Total time: %d msec"%(1000*(time()-start_time))