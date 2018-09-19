import psyco
psyco.full()

f = open('A-large.in')
lines = f.read().splitlines()
f.close()

f = open('A.out','w')

T = int(lines.pop(0))

num1 = lambda x1,y1,x2,y2,x3,y3,x4,y4: ((x1*y2-y1*x2)*(x3-x4) - (x1 - x2)*(x3*y4-y3*x4))
num2 = lambda x1,y1,x2,y2,x3,y3,x4,y4: ((x1*y2-y1*x2)*(y3-y4) - (y1 - y2)*(x3*y4-y3*x4))
denom = lambda x1,y1,x2,y2,x3,y3,x4,y4: (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
isGood = lambda x1,y1,x2,y2,x3,y3,x4,y4: round(denom(x1,y1,x2,y2,x3,y3,x4,y4),7) != 0

def P(x1,y1,x2,y2,x3,y3,x4,y4):
    d = denom(x1,y1,x2,y2,x3,y3,x4,y4)
    
    if round(d,7) == 0:
        return None, None
        
    n1 = num1(x1,y1,x2,y2,x3,y3,x4,y4)
    n2 = num2(x1,y1,x2,y2,x3,y3,x4,y4)
    
    return (n1/d, n2/d)
    
for t in xrange(T):
    N = int(lines.pop(0))
    #print "N",N
    count = 0
    Ls = []
    
    for i in xrange(N):
        y1, y2 = [int(x) for x in lines.pop(0).split()]
        Ls.append((0.0, y1, 10.0, y2))
        #print "y1 y2", y1,y2
        
    for i in xrange(N):
        x1,y1,x2,y2=Ls[i]
        for k in xrange(i+1, N):
            x3,y3,x4,y4 = Ls[k]
            x,y = P(x1,y1,x2,y2,x3,y3,x4,y4)
            
            if (0 < x) and (x < 10) and (min(y1,y2,y3,y4) < y) and (y < max(y1,y2,y3,y4)):
                count+=1

            #    count+=1
         
    f.write('Case #%d: %s\n' % (t+1,count))

f.close()

#print '\n'.join(results)+'\n'
