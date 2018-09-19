#!/usr/bin/python

infile = open("A.in", "rt")
outfile = open("A.out", "wt")

ii = int(infile.readline())

for i in range(ii):
    kk = int(infile.readline().strip('\n'))
    team = []
    for k in range(kk):
        team.append(infile.readline().strip('\n'))
    
    WP = []
    for k in range(kk):
        a = team[k].count('1')
        b = team[k].count('0')
        WP.append(a / (a + b))

    OWP = []
    for k in range(kk):
        c = kk - team[k].count('.')
        z = []        
        for j in range(kk):            
            if team[k][j] == '0' or team[k][j] == '1':
              a = team[j].count('1')
              b = team[j].count('0')
              if team[j][k] == '0':
                  b = b - 1
              if team[j][k] == '1':
                  a = a - 1

              z.append(a / (a + b))

        s = 0
        for y in z:
            s = s + y
        OWP.append(s / c)
    
    OOWP = []
    for k in range(kk):
        s = 0
        c = kk - team[k].count('.')
        for j in range(kk):
            if team[k][j] == '0' or team[k][j] == '1':                
                s = s + OWP[j] 

        OOWP.append(s / c)
    
    outfile.write("Case #%s: \n" % (i + 1))
    for f in range(kk):
        outfile.write('%s\n' % (0.25 * WP[f] + 0.5 * OWP[f] + 0.25 * OOWP[f]))
        
    
    
