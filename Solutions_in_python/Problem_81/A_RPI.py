from sys import stdout

ifile = open('../input/A-large.in', 'r')
ofile = open('../output/A-large.out', 'w')
#ofile = stdout

cases = int(ifile.readline())

for case in xrange(cases):
    n = int(ifile.readline())
    teams = []
    opponents = []    
    for team in xrange(n):
        teams.append([0, 0])
        olist = []
        line = ifile.readline().strip()
        #print line
        for i, c in enumerate(line):            
            if c == '.': 
                continue
            else: 
                v = int(c)
                teams[team][v] += 1
                olist.append((i, v))
        opponents.append(olist)
    ofile.write('Case #%d:\n' % (case+1))
    wp = []
    owp = []
    oowp = []
    for team in xrange(n):
        s = teams[team]
        wp.append(float(s[1]) / (s[0] + s[1]))            
        #print "WP %d = %f"  % (team, wp[team])    
    for team in xrange(n):
        v = 0.0;
        vc = 0;       
        for o in opponents[team]:
            s = teams[o[0]]            
            if o[1]:
                xwp = float(s[1]) / (s[0] + s[1] - 1)
            else:
                xwp = float(s[1] - 1) / (s[0] + s[1] - 1)
            #print s
            #print "..XWP %d (%d) %f" % (o[0], o[1], xwp)         
            v += xwp  
            vc += 1       
        owp.append(float(v) / vc)
        #print "OWP %d = %f"  % (team, owp[team])        
    for team in xrange(n):
        v = 0.0;
        vc = 0
        for o in opponents[team]:
            v += owp[o[0]]
            vc += 1
        oowp.append(float(v) / vc)    
        #print "OOWP %d = %f"  % (team, oowp[team])
        rpi = 0.25 * wp[team] + 0.5 * owp[team] + 0.25 * oowp[team]
        ofile.write("%.12f\n" % rpi)
    #print seconds
    
