f = open("B-small-attempt6.in")
data = f.readlines()
f.close()

data = map(str.strip, data) # strip newline char

resout = []
for testcase in data[1:]:
    print
    print "TESTCASE"
    ar = testcase.split(' ')
    
    numbaseelements = int(ar[0])
    # if numbaseelements:
    baseelements = ar[1:1+numbaseelements]
    numopposingelements = int(ar[1+numbaseelements])
    # if numopposingelements:
    opposingelements = ar[2+numbaseelements:2+numbaseelements+numopposingelements]
    numchars = int(ar[2+numbaseelements+numopposingelements])
    sequence = list(ar[-1])
    
    print ar
    print "Number of base elemenets:", numbaseelements
    print "  base elements:", baseelements
    be = {}
    for baseelement in baseelements:
        be[baseelement[0]+baseelement[1]] = baseelement[2]
        be[baseelement[1]+baseelement[0]] = baseelement[2]
    print be
    
    print "Number of opposing elements:", numopposingelements
    print "  opposing elements:", opposingelements
    oe = {}
    for opposingelement in opposingelements:
        oe[opposingelement[0]] = opposingelement[1]
        oe[opposingelement[1]] = opposingelement[0]
    print oe

    print "Number of sequence chars:", numchars
    print "  sequence:", sequence
    
    outseq = [sequence.pop(0)]
    startop = []
    if outseq[0] in oe:
        startop.append((outseq[0], 0))
    print startop
    print outseq
    print sequence
    for e in sequence:
        print "processing:", e
        if outseq and outseq[-1]+e in be:
            try:
                startop.remove((outseq[-1], len(outseq)-1))
            except ValueError:
                pass
            outseq[-1] = be[outseq[-1]+e]
            # startop = None
            print outseq
            continue
            
        if e in oe:
            did = False
            tmpstartop = startop[:]
            # tmpstartop.reverse()
            for s in tmpstartop:
                if s[0] != e:
                    outseq = outseq[:s[1]]
                    startop.remove(s)
                    outseq = []
                    startop = []
                    print "cutting", startop
                    did = True
                    break
            if did: 
                continue
            
            startop.append((e, len(outseq)))
            print "Setting startop at", startop
        
        print "adding:",e
        outseq.append(e)
    print outseq
        
        
    
    
    # i = 0
    # seqlen = len(sequence)
    # while i < seqlen-1:
    #     # print sequence[i]
    #     # print sequence[i]+sequence[i+1]
    #     if (sequence[i]+sequence[i+1]) in be:
    #         print "inside if",be[sequence[i]+sequence[i+1]]
    #         sequence[i] = be[sequence[i]+sequence[i+1]]
    #         sequence.pop(i+1)
    #         i = 0
    #         seqlen = len(sequence)
    #         continue
    #     if sequence[i] in oe:
    #         print "looking for opposing elements for ", sequence[i]
    #         try:
    #             oeidx = sequence.index(oe[sequence[i]])
    #         except ValueError:
    #             i += 1
    #             continue
    #         if oeidx < len(sequence)-1:
    #             print "got an opposing element at", oeidx
    #             sequence = sequence[oeidx+1:]
    #             i = 0
    #             seqlen = len(sequence)
    #             print sequence
    #             continue
    #     i += 1
    # # fix the last opposing
    # if sequence[-1] in oe:
    #     print "in the last opposing"
    #     tmpseq = sequence[:]
    #     tmpseq.reverse()
    #     print tmpseq
    #     try:
    #         oeidx = tmpseq.index(oe[sequence[-1]])
    #     except ValueError:
    #         print "Value error"
    #         pass
    #     else:
    #         if oeidx < len(sequence)-1:
    #             tmpseq = tmpseq[oeidx+1:]
    #     tmpseq.reverse()
    #     sequence = tmpseq[:]
    # print sequence
    # resout.append(sequence)
    resout.append(outseq)


f = open("B-small-attempt6.out", 'w')
for i, res in enumerate(resout):
    f.write("Case #%d: [%s]\n" % (i+1, ', '.join(res)))
f.close()

print "FILE WRITTEN!"    
    
    