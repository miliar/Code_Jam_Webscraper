fileLoc = '/Users/alarobric/Downloads/'
#fileLoc += 'A-small-attempt0'
#fileLoc += 'A-test'
fileLoc += 'A-large'
f = open(fileLoc+'.in', 'r')
g = open(fileLoc+'.out', 'w')
 
cases = int(f.readline())
 
for i in range (1, cases + 1):
    result = "Broken"
    [N, Pd, Pg] = [int(c) for c in f.readline().split()]
    #print "N, Pd, Pg", N, Pd, Pg
    
    for j in xrange(1, min(101,N+1)):
        wonTodayRemain = (j * Pd) % 100
        #print j, wonTodayRemain
        if (0 == j % 1000): print j
        if (wonTodayRemain == 0):
            #possible denominator - now playedEver >= j,   and wonEver >= wonToday,     wonEver/playedEver = Pg
            #print "possible for today"
            #wonToday = j*Pd / 100
            
            if not((Pg == 0) and (Pd != 0)) and not ((Pg == 100) and (Pd != 100)):
                result = "Possible"
                break
        if j > 100:
            print "AHHHHHHHHHHHHHHHHHHHHHHH"
    
    
    output = "Case #" + str(i) + ": " + result + "\n"
    print output
    g.write(output)
    
#3
#1 100 50
#10 10 100
#9 80 56