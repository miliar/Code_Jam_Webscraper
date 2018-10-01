f = open('A-large.in', 'r')

T = int(f.readline().strip())



for t in xrange(T):

    line = f.readline().strip()    
    sh = [int(x) for x in line.split(" ")[1]]

    tot = 0
    tots = 0
    for idx, sh_i in enumerate(sh):
        if idx <= tot:
            tot += sh_i
        else:
            s = idx - tot
            tots += s
            tot += sh_i + s

    print 'Case #%d: %d'% (t+1,tots)