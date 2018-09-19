import sys

def prod(p):
    r = 1
    for i in p:
        r *= i
    return r

def keep(a, b, p):
    p0 = prod(p)
    rem = b-a+1
    return p0*rem + (1-p0)*(rem+b+1)

def bs(i, a, b, p):
    if i==0:
        return keep(a, b, p)
    #return 1 + bs(i-1, a-1, b, p[:-1])
    p0 = prod(p[:-i])
    rem = b-a+1+i+i
    return p0*rem + (1-p0)*(rem+b+1)
    

data = sys.stdin.readlines()
n = int(data[0])
#print n
for i in range(n):
    a, b = map(int, data[2*i+1].split())
    p = map(float, data[2*i+2].split())
    r = b+2.0 # press enter
    #print r
    for j in range(a+1):
        t = bs(j, a, b, p)
        #print j, t
        r = min(r, t)
    print "Case #%d: %.6f" % (i+1, r)
