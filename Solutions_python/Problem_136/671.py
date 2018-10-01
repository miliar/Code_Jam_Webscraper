def nFarms(c,f,x,k):
    return sum([f/(2+i*x) for i in xrange(k)])+c/(2+k*x)

for t in xrange(1,input()+1):
    f, x, c = map(float, raw_input().split())
    k = int(c/f-2/x)
    farms = min( [ nFarms(c,f,x,i) for i in map( lambda x: max(0,x), [k-1, k, k+1] ) ] )
    print 'Case #'+str(t)+': %.07f'%(farms)




