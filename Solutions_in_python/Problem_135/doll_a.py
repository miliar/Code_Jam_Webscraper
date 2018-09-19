filename = 'A-small-attempt0.in' #raw_input()
with open (filename) as f:
    T = int(f.readline())
    for icase in range(T):
        lcards = [0]*17
        r = int(f.readline())
        for i in range(4):
            line = f.readline()
            if i+1 == r:
                rcards = line.split()
                for card in rcards:
                    lcards[int(card)]+=1
        r = int(f.readline())
        for i in range(4):
            line = f.readline()
            if i+1 == r:
                rcards = line.split()
                for card in rcards:
                    lcards[int(card)] += 1
        if lcards.count(2) < 1:
            print 'Case #%s: %s' % (icase+1 ,'Volunteer cheated!')
        elif lcards.count(2) > 1:
            print 'Case #%s: %s' % (icase+1 ,'Bad magician!')
        else :
            print 'Case #%s: %s' % (icase+1 ,lcards.index(2))
