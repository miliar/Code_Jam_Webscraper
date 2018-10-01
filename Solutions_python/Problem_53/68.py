def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

nt = readint()

for i in range(nt):
    ns, nf = tuple(readints())
    sw = (1 << ns)-1
    if (sw & nf) == sw :
        a = "ON"
    else:
        a = "OFF"
    print "Case #%d: %s" % (i+1, a)

