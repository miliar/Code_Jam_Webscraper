import sys

#fp = open('test.in')
fp=sys.stdin

T = int(fp.readline())

def is_tidy(sn):
    dn= sn[0]
    for sni in sn:
        if sni< dn:
            return False
        else:
            dn=sni
    return True

def get_tidy(sn):
    i,si = 0,sn[0]
    while i<len(sn)-1 and si<= sn[i+1]:
        i+=1
        si=sn[i]
    if i==len(sn)-1:
        return sn
    if si==0:
        i-=1
        si=sn[i]

    si-=1
    sn[i]= si
    i+=1
    while i < len(sn):
        sn[i]=9
        i+=1

    if is_tidy(sn):
        if sn[0]==0:
            sn.pop(0)
        return sn

    return get_tidy(sn)
"""
tm = 346
st = [int(i) for i in str(tm)]
print get_tidy(st)
exit(1)
"""

for t in xrange(T):
    N= list([int(i) for i in fp.readline().rstrip()])
    res= get_tidy(N)
    sres = ''.join([str(i) for i in res])
    print "Case #%d: %s"%(t+1,sres)


