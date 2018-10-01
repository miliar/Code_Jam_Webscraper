import sys

f = open(sys.argv[1],'r')

N=int(f.readline())

for cas in xrange(1,N+1):
    l=f.readline().strip().split()
    dict_c = {}
    dict_o = {}
    n = int(l[0])
    i = 1
    while n>0:
        s=l[i]
        dict_c[s[:2]] = s[2:]
        n = n-1
        i = i+1
    n = int(l[i])
    i = i + 1
    while n>0:
        s = l[i]
        dict_o[s] = ''
        n = n - 1
        i = i + 1
    s = l[i+1]
    r = ''
    for t in s:
        if len(r)>0:
            v=r[-1]+t
            v2 = t+r[-1]
            if v in dict_c:
                r = r[:-1]+dict_c[v]
            elif v2 in dict_c:
                r = r[:-1]+dict_c[v2]
            else:
                r = r + t
                for x in r:
                    v = x+t
                    v2 = t+x
                    if v in dict_o or v2 in dict_o:
                        r = ''
                        break
        else:
            r = r + t
    print "Case #"+str(cas)+": ["+", ".join(list(r))+"]"

