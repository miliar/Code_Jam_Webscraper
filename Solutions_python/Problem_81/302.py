import sys

# read int
cases = int(sys.stdin.readline().strip())

for case in range(cases):
    n = int(sys.stdin.readline().strip())
    table = [] 
    wins = [0 for i in range(n)]
    loose = [0 for i in range(n)]
    for i in range(n):
        line = sys.stdin.readline().strip()
        table.append(line)
        for j in range(n):
            if table[i][j] == '1':
                wins[i] = wins[i] + 1
            elif table[i][j] == '0':
                loose[i] = loose[i] + 1

    #print table
                
    OWP = [0 for i in range(n)]
    for i in range(n):
        OWPsum = 0
        OWPcount = 0
        for j in range(n):
            if table[i][j] == '1':
                OWPsum = OWPsum + float(wins[j])/(wins[j] + loose[j] - 1)
                OWPcount = OWPcount + 1
            elif table[i][j] == '0':
                OWPsum = OWPsum + float(wins[j] - 1)/(wins[j] + loose[j] - 1)
                OWPcount = OWPcount + 1
            else:
                pass
        #print i, OWPsum, OWPcount
        OWP[i] = OWPsum / OWPcount
    
    #print OWP

    print 'Case #%d:' % (case + 1)    
    for i in range(n):
        OOWPsum = 0
        OOWPcount = 0
        for j in range(n):
            if table[i][j] != '.':
                OOWPsum = OOWPsum + OWP[j]
                OOWPcount = OOWPcount + 1
        WP_ = float(wins[i]) / (wins[i] + loose[i])
        OWP_ = OWP[i]
        OOWP_ = OOWPsum / OOWPcount
        #print WP_, OWP_, OOWP_
        print 0.25 * WP_ + 0.50 * OWP_ + 0.25 * OOWP_
        
