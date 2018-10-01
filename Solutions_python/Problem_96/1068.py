import StringIO, sys

if len(sys.argv)>1:
    input = file(sys.argv[1])
else:
    input = StringIO.StringIO("""4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21""")

def maxNotSurprising(n):
    b = n / 3
    #1: 0+0+1
    #2: 0+1+1
    if n%3>0:
        return b+1
    #0+0+0
    return b

def maxSurprising(n):
    b = n / 3
    #2: 0+0+2
    if n%3==2:
        return b+2
    #1: 0+1+0
    if n%3==1:
        return b+1
    #3: 0+1+2
    if n%3==0 and n>0:
        return b+1
    #0: 0+0+0
    return b

def solve(s, p, ti):
    #print "s:%d, p:%d, ti:%s" % (s, p, ti)
    c = 0
    for t in ti:
        maxNot = maxNotSurprising(t)
        maxSur = maxSurprising(t)
        #print "\tt:%d, s:%d, maxNot: %d, maxSur: %d" % (t, s, maxNot, maxSur)
        if s>0 and maxSur>maxNot and maxSur>=p and maxNot<p:
            if maxSur >= p:
                c+=1
                s-=1
        else:
            if maxNot>=p:
                c+=1
    return c

for case in range(int(input.readline())):
    values = [int(x) for x in input.readline().split()]
    print "Case #%d: %d" % (case+1, solve(values[1], values[2], values[3:]))
            
