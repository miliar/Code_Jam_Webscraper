
def Magicka():
    it = iter(raw_input().split())
    C = {}
    for i in xrange(int(it.next())):
        a, b, c = it.next()
        C[a+b] = c
        C[b+a] = c
    D = {}
    for i in xrange(int(it.next())):
        a, b = it.next()
        D[a] = D.get(a, "") + b
        D[b] = D.get(b, "") + a
    it.next()
    result = ""
    for invoke in it.next():
        result += invoke
        c = C.get(result[-2:])
        if c:
            result = result[:-2] + c
            continue
        for opp in D.get(invoke, ""):
            if opp in result:
                result = ""
                break
    print "[" + ", ".join(result) + "]"

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    Magicka()
