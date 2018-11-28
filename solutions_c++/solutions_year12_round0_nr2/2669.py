inp = file('B-small-0.in')
out = file('B-small-0.out', 'w')

t = int(inp.readline())
for cas in range(1, t+1):
    lin = map(int, inp.readline().split())
    N = lin[0]
    S = lin[1]
    p = lin[2]
    marks = lin[3:]
    avg = [m/3 for m in marks]
    rem = [m%3 for m in marks]
    #print 'N total: ', N
    #print 'Special: ', S
    #print 'p Minim: ', p
    #print 'average: ', avg
    #print 'remainder: ', rem
    ts = 0 #special done
    tp = 0 #answer
    for i in range(N):
        av = avg[i]
        re = rem[i]
        if av >= p:
            tp+=1
            #print 'normal\n\tpos: ',i,' av: ',av
        elif re:
            if re == 1 and av + re >= p:
                tp += 1
                #print '+1 rem\n\tpos: ',i,' av: ',av
            elif re == 2 and av + 1>=p:
                tp += 1
                #print '+1 rem with rem 2\n\tpos: ',i,' av: ',av
            elif re == 2 and av + re>=p and ts < S:
                ts+=1
                tp += 1
                #print '+2 rem\n\tpos: ',i,' av: ',av, ' ts: ', ts
        else:
            if re == 0 and av - 2 > 0 and av + 2 >= p and ts < S:
                ts += 1
                tp += 1
                #print 're = 0 special\n\tpos: ',i, 'av: ', av, ' ts: ',ts
    out.write('Case #%d: '%cas+str(tp)+'\n')

