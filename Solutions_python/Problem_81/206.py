import sys


def solve(teams, data):
#    print teams
 #   print data

    wp = []
    owp = []
    oowp = []
    rpi = []

    for l in data:
        won = 0
        lost = 0
        for x in xrange(len(l)):
            if l[x] == '1':
                won += 1
            if l[x] == '0':
                lost += 1
        wp.append((float(won)) / (won + lost))

    for l, dl in enumerate(data):
        twp = [0] * teams
        divby = 0
        for t, dt in enumerate(data):
            won = 0
            lost = 0

            played_against = False
            for x in xrange(len(dt)):
                if x == l:
                    if dt[x] != ".":
                        played_against = True
                    continue
                
                if dt[x] == '1':
                    won += 1
                if dt[x] == '0':
                    lost += 1

            if (played_against):
                divby += 1
            
#            if l==3:
 #               print t, won, lost
            if t != l and played_against:
                twp[t] = (float(won)) / (won + lost)
  #      print twp

        owp.append( float(sum(twp)) / (divby) )


    for l, dl in enumerate(data):
        sm = 0
        ln = 0
        for x in xrange(teams):
            if dl[x] != ".":
                sm += owp[x]
                ln += 1
            
        oowp.append( (float(sm) / ln ) )
        
    for l in xrange(teams):
        rpi.append( (0.25 * wp[l]) + (0.5 * owp[l]) + (0.25 * oowp[l]) )

#    print rpi
#    print owp            
#    print wp

    return rpi

        
def main():
    fd = open(sys.argv[1], "r")
    entries = int(fd.readline())

    for i, entry in enumerate(xrange(entries)):
        teams = int(fd.readline())

        data = [fd.readline().strip() for team in xrange(teams)]
        
        result = solve(teams, data)

        print "Case #%d: " % (i + 1)
        for x in result:
            print x

if __name__ == "__main__":
    main()
