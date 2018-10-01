import psyco

f = open("input.txt")

numcases = int(f.readline())

for case in xrange(numcases):
    line = f.readline()
    line = line.split(" ")

    numbuttons = int(line[0])

    line = line[1:]

    bpos = 1
    opos = 1

    btime = 0
    otime = 0

    bchange = 0
    ochange = 0

    dtime = 0
    
    for i in xrange(numbuttons):
        index = i*2
        newpos = int(line[index+1])
        if line[index] == 'O':
            if ochange > 0:
                dtime = 1 + abs(opos - newpos)
                ochange += dtime
                otime += dtime
                opos = newpos
##                print "O kept moving to %d (+%d)" % (newpos, dtime)
            else:
                if bchange >= abs(opos-newpos):
                    ochange = 1
                    otime = btime + 1
                else:
                    ochange = max(1,1 + abs(opos-newpos) - bchange)
                    otime = btime
                    otime += ochange
                opos = newpos
##                print "O moved to %d (+%d)" % (newpos, ochange)
            bchange = 0                
        elif line[index] == 'B':
            if bchange > 0:
                dtime = 1 + abs(bpos - newpos)
                bchange += dtime
                btime += dtime
                bpos = newpos
##                print "B kept moving to %d (+%d)" % (newpos, dtime)
            else:
                if ochange >= abs(bpos-newpos):
                    bchange = 1
                    btime = otime + 1
                else:
                    bchange = max(1,1 + abs(bpos-newpos) - ochange)
                    btime = otime
                    btime += bchange
                bpos = newpos
##                print "B moved to %d (+%d)" % (newpos, bchange)
            ochange = 0
                
        else:
            print "error: bot %s. Case %d. Index %d" % (line[case], case, index)

    print "Case #%d: %d" %(case + 1, max(btime, otime))

f.close()
