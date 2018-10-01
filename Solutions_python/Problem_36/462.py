import sys

N = int(sys.stdin.readline().strip())

#print N

S = "welcome to code jam"
D = {}
for x in xrange(0,len(S)):
    if D.has_key(S[x]):
        D[S[x]] += 1
    else:
        D.update({S[x]:1})
#print D


def bk(s, si=0,i=0):
#    print i, si, "#"*4
    global cont
    global S
    if i >= len(S):
#        print "match"
        cont += 1
        return False

    b = True
    for x in xrange(si,len(s)):
#        print x, i
#        print s[x], S[i]
        if s[x] == S[i]:
            b = bk(s, x, i+1)

for x in xrange(0,N):
    s = sys.stdin.readline().strip()
    s2 = ""
    for i in xrange(0,len(s)):
        if D.has_key(s[i]):
            s2 += s[i]
#    print s2
    cont = 0
    bk(s)
    print "Case #%d: %04d" % (x+1,cont)
