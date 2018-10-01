'''
Created on Apr 8, 2017

@author: davidkogosov
'''
from Tkconstants import LAST

count = 1
dict = {}

def process(filename):
    f = open(filename)
    num = int(f.readline())
    #print 'num', num
    for i in range(num):
        l = f.readline()
        solve(int(l))
    f.close()
    
    
def solve(n):   
    global count 
    out = 'Case #' + str(count) + ":"
    print out, sol___(n)
    count += 1


def sol(n):
    global dict
    max = 1
    i = 1
    while i<= n:
        #print n+1-i
    #for i in xrange(1, n+1):
        
        if (n+1-i) in dict:
            return dict[n+1-i]
        #print n+1-i
        rc = issorted3(n+1-i)
        if rc == 0:
            max = n+1-i
            break
        elif rc == 1:
            i += 1
        else:
            i += 10**(rc-1) 
    
    mmax = max
    #print max, n+1
    for i in xrange(max,n+1):
         #print i
         if issorted2(i):
             mmax = i
  
    dict[n] = mmax
    
    return mmax        
    
    
    
def sol___(n):
    global dict
    max = 1
    for i in xrange(1, n+1):
        
        if (n+1-i) in dict:
            return dict[n+1-i]
        #print n+1-i
        if issorted2(n+1-i):
            max = n+1-i
            break
    
    dict[n] = max
    #print dict
    return max





def sol_(n):
    max = 1
    R = 10000000000
    
    if n < R:
        return sol2(n)
    
    for i in xrange(1, n+1, 1000000000):
        #print n+1-i
        if issorted2(n+1-i):
            max = n+1-i
            break
        
    mmax = max
    for i in xrange(max + 1, max + R + 1):
        if issorted2(i):
            mmax = i
            
    return mmax

def sol2(n):
    max = 1
    for i in xrange(1,n+1):
        if issorted2(i):
            max = i
            
    return max    



def issorted(i):
    global dict
    if i in dict:
        return dict[i]
    
    lst = tolist(i)
    #print i, lst
    for k in range(len(lst)-1):
        if lst[k+1] > lst[k]:
            dict[i] = False
            return False
    dict[i] = True
    return True

def issorted3(n):
    lst = tolist(n)
    
    last = lst[len(lst)-1]
    for i in range(2, len(lst)+1):
        curr = lst[len(lst) - i]
        if curr < last:
            return len(lst) - i + 1
        last = curr
        
    return 0
    
             
        

def tolist(i):
    lst = []
    
    while i>0:
        lst.append(i%10)
        i /= 10
    return lst        

def issorted2(i):
    #if i%1000000 == 0: 
    #    print i
    last = 10
    
    #return False
    
    while i > 0:
        curr = i%10
        if curr > last:
            return False
        last = curr
        i /= 10
        
    return True

def filldict():
    global dict
    
    for i in range(18):
        sol___(10**i)
    
if __name__ == '__main__':
    #print sol(866)
    #print issorted3(1000)
    filldict()
    #print dict
    #for i in xrange(0, 10000000000000, 1000000000):
    #   print "solution for ", i, " is", sol(i)
    process('/Users/davidkogosov/Downloads/B-small-attempt2.in')