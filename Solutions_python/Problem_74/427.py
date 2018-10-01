reader = open('A-large.in')
writer = open('output-A-large', 'w')

test_cases = int(reader.readline())

for kount in range(test_cases):
    line = reader.readline()[:-1].split(' ')[1:]
    
    turns = 1
    bpos = 1
    opos = 1

    bobj = 0
    oobj = 0

    # index for b and o step
    bi = 9999
    oi = 9999

    while len(line) > 0:

        # get orange objective
        for i in range(0, len(line), 2):
            if line[i] == 'O':
                oobj = int(line[i+1])
                oi = i + 1
                break

        # get blue objective
        for i in range(0, len(line), 2):
            if line[i] == 'B':
                bobj = int(line[i+1])
                bi = i + 1
                break

        # print 'B to %s, O to %s' % (bobj, oobj)

        #print line
        #print oi, bi

        # pushed button?
        p = False

        # execute step for orange
        if oobj > opos:
            opos += 1
        elif oobj < opos:
            opos -= 1
        else:
            if oi < bi:
                #print 'O pushed %s' % (line[1])
                line = line[2:]
                p = True
                oi = 9999

        # execute step for blue
        if bobj > bpos:
            bpos += 1
        elif bobj < bpos:
            bpos -= 1
        else:
            if bi < oi and not p:
                #print 'B pushed %s' % (line[1])
                line = line[2:]
                bi = 9999

        turns += 1

    writer.write('Case #%s: %s' % (str(kount + 1), str(turns - 1)) + '\n')

writer.close()
reader.close()
