#!/usr/bin/python2.7

T = int(raw_input())
for case in range(T):
    N = int(raw_input())
    crosstable = {}
    for i in range(N):
        row = raw_input()
        for j in range(N):
            if row[j] != '.':
                if j not in crosstable:
                    crosstable[j] = {}
                if i not in crosstable:
                    crosstable[i] = {}
                if row[j] == '1':
                    crosstable[i][j] = 1
                    crosstable[j][i] = 0
                elif row[j] == '0':
                    crosstable[i][j] = 0
                    crosstable[j][i] = 1

    total_score = {}
    num_opponents = {}
    WP = {}
    OWP = {}
    OOWP = {}
    for i in range(N):
        total_score[i] = reduce(lambda x, y: x + y, crosstable[i].values())
        num_opponents[i] = len(crosstable[i])
    for i in range(N):
        WP[i] = total_score[i] / float(num_opponents[i])
    for i in range(N):
        OWP[i] = 0
        #print "Calculating OWP for Team %d" % (i + 1)
        for opponent in crosstable[i].keys():
            OWP[i] = OWP[i] + ((total_score[opponent] - crosstable[opponent][i]) / float(num_opponents[opponent] - 1))
            #print "Team %d had WP %f without considering matches against %d" % (opponent, ((total_score[opponent] - crosstable[opponent][i]) / float(num_opponents[opponent] - 1)) , i)
        OWP[i] = OWP[i] / float(num_opponents[i])
    for i in range(N):
        OOWP[i] = reduce(lambda x, y: x + y, [OWP[j] for j in range(N) if j in crosstable[i].keys()]) / float(len(crosstable[i]))

    print "Case #%d:" % (case + 1)
    #print crosstable
    for i in range(N):
        #print "Team %d: WP=%f, OWP=%f, OOWP=%f" % ((i + 1), WP[i], OWP[i], OOWP[i])
        print float(((0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i])))

