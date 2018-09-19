def probleme1(file):
    with open(file) as f:
        data =  [line[:11].split() for line in f]
        i = 0
        while i <  int(data[0][0]):
            raw1 = int(data[1+10*i][0])
            raw2 = int(data[6+10*i][0])
            s = list(set(data[1+10*i+raw1]) & set(data[6+10*i+raw2]))
            i += 1
            if (len(s) == 0):
                print "Case #%d: Volunteer cheated!" % i
            if (len(s) == 1):
                print "Case #%d: %d" % (i,int(s[0]))
            if (len(s) > 1):
                print "Case #%d: Bad magician!" % i
probleme1("A-small-attempt0.in")
