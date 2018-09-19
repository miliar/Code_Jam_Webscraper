fl=raw_input()
[L,D,N]=[int(e) for e in fl.split()]
#print L,D,N

allword=[]
for i in xrange(D):
    allword.append(raw_input())

(INSIDE, OUTSIDE)=(1,2)
for i in xrange(N):
    q=raw_input()
    pattern=[]

    state=OUTSIDE
    for w in q:
        if w=="(":
            state=INSIDE
            pattern.append([])
            continue
        elif w==")":
            state=OUTSIDE
            continue
        else:
            if state==INSIDE:
                pattern[-1].append(w)
            else:
                pattern.append([w])

    if len(pattern)>L:
        print "Case #%d: %d" % i+1, 0
    else:
        ok=0
        for word in allword:
            for index, w in enumerate(word):
                if w in pattern[index]:
                    continue
                else:
                    break
            else:
                ok+=1
        print "Case #%d: %d" % (i+1, ok)
            
