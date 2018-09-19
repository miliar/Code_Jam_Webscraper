#from sys import stdin as inp
inp = file("A-large.in", 'r')
out = file("A-large.out", 'w')
t =  int(inp.readline())
for t1 in xrange(1, t+1):
    r, c, w = map(int, inp.readline().split())
    ans = (r-1)*(c/w)
    ans = ans + w
    ans = ans + (c-1)/w
#    print "Case #%d: %d\n"%(t1, ans)
    out.write("Case #%d: %d\n"%(t1, ans))
inp.close()
out.close()
