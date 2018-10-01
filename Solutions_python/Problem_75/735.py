f = open("B.in","r")
f2 = open("B.out","w")

base = list("QWERASDF")
def solve(l):
    r = []
    
    c = int(l.pop())
    combine = dict()
    for i in xrange(c):
        elem = list(l.pop())
        word = elem[0:2]
        word.sort()
        combine[''.join(word)] = elem[2]
    
    d = int(l.pop())
    oppose = []
    for i in xrange(d):
        elem = list(l.pop())
        elem.sort()
        oppose.append( ''.join(elem) )
    l.pop()
    w = list(l.pop())
    #print "\n\n"
    while ( len(w) > 0 ):
        r.append( w[0] )
        w = w[1:]
        if ( len(r) < 2 ):
            continue
        #print r , ''.join(r[-2:]), combine
        sliced = r[-2:]
        sliced.sort()
        sliced = ''.join(sliced)
        if sliced in combine:
            r = r[:-2] + [ combine[ sliced ] ]
        else:   
            for ch in r[:-1]:
                tmp = [ch, r[-1]]
                tmp.sort()
                if ''.join(tmp) in oppose:
                    r = []
                    break

    return r

for idx in xrange(int(f.readline().strip())):
    l =  f.readline().strip().split()
    l.reverse()
    l2 = solve(l)
    
    f2.write( "Case #%d: " % (idx+1) )
    f2.write( str(l2).replace("\'","") )
    f2.write( "\n" )

f2.close()
f.close()
