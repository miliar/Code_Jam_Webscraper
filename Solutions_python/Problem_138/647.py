import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        score_war = 0
        score_deceitful = 0
        f.readline()
        Naomi = [float(x) for x in f.readline().split()]
        Naomi.sort()
        Ken = [float(x) for x in f.readline().split()]
        Ken_war = sorted(Ken)
        for n in reversed(Naomi):
            k = Ken_war[-1]
            if n > k:
                score_war += 1
            else:
                Ken_war.pop()
        Ken_deceitful = sorted(Ken, reverse=True)
        for n in Naomi:
            k = Ken_deceitful[-1]
            if n > k:
                score_deceitful += 1
                Ken_deceitful.pop()
        print "Case #%d: %d %d" % (i+1, score_deceitful, score_war)
