import sys

n = int(sys.stdin.readline())

for i in xrange(1,n+1):
    dic={}
    li = sys.stdin.readline().strip()
    l = [None]*len(li)

    l[0]=1
    dic[li[0]] = 1
    nex = 0
    for j,x in enumerate(li):
        if j==0:
            continue
        if x in dic:
            l[j]=dic[x]
        else:
            dic[x] = nex
            l[j] = nex
            if nex == 0:
                nex = 2
            else:
                nex += 1

    if nex < 2:
        nex = 2

    val = 0
    mult = 1
    for j in l[::-1]:
        val += mult*j
        mult *= nex

    print "Case #%d: %d" % (i,val)#

