import sys


N = int(sys.stdin.readline().strip())
for f in range(1, N+1):
    print 'Case #%d:' % f,

    input  = map (int, sys.stdin.readline()[:-1].split(' '))

    ok =0
    l=[]
    for i in xrange(input[0], input[1]+1):
        number = i
        for j in xrange(1,len(str(i))):
            number = int(str(i)[j:]+str(i)[:j])
            if (i < number and input[0]<=number and number<=input[1]):
                l.append((i,number))
                ok+=1
            
    print len(set(l))  
