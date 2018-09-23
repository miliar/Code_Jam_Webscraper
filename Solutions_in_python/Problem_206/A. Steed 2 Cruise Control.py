f = open('A-large (1).in', 'r')
g = open('A-large (1).out', 'w')
t_c = int(f.readline().strip())

a = 1
while a <= t_c:
    line1 = f.readline().strip().split()
    D = int(line1[0])
    N = int(line1[1])
    b = 0
    lastH = 0
    while b < N:
        line2 = f.readline().strip().split()
        K = int(line2[0])
        S = int(line2[1])
        if (D - K)/float(S) > lastH:
            lastH = (D - K)/float(S)
        b += 1
    t = "%.6f" % (D/lastH)
    g.write("Case #"+str(a)+': '+str(t)+'\n')
    #print t
    
    a += 1
g.close()    