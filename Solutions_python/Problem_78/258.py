f = open("g_A.in","r")
f2 = open("g_A.out","w")
f.readline()

def solve(N,pd,pg):

    for i in xrange(1,N+1):
        #i 
        if (i * pd) % 100 == 0:
            for j in xrange(0 , i*99+1):
                if ((i+j) * pg) % 100 == 0 \
                and ((i+j) * pg) / 100 >= i*pd/100 \
                and ((i+j) * (100-pg)) / 100 >= i*(100-pd)/100: 
                    print i,j
                    return "Possible"

    return "Broken"

idx = 0
for l in f:
    N , pd,pg = map(int,l.strip().split())
    out = solve(N,pd,pg)
    idx += 1
    f2.write( "Case #%d: %s\n" % (idx,out) )

f2.close()

f.close()
