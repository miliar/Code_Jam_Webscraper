#!/usr/local/bin/python

from sys import stdin

lines = stdin.read().splitlines()
num_tests = int(lines[0])
for test in xrange(num_tests):
    test_row = test * 3 + 1
    naomi = map(float, lines[test_row + 1].split())
    ken = map(float, lines[test_row + 2].split())
    max_naomi = sorted(naomi, reverse=True)
    max_naomi2 = list(max_naomi)
    max_ken = sorted(ken, reverse=True)
    max_ken2 = list(max_ken)
    cheat_score = 0
    while len(max_naomi) > 0:
        #print "Naomi", max_naomi
        #print "Ken", max_ken
        #print cheat_score
        if(max_naomi[0] > max_ken[0]):
            max_naomi.pop(0)
            max_ken.pop(0)
            cheat_score += 1
        else:
            max_naomi.pop(-1)
            max_ken.pop(0)
    score = 0
    while len(max_naomi2) > 0:
        if(max_naomi2[0] > max_ken2[0]):
            max_naomi2.pop(0)
            max_ken2.pop(-1)
            score += 1
        else:
            max_naomi2.pop(0)
            max_ken2.pop(0)
    print "Case #{0}: {1} {2}".format(test + 1, cheat_score, score)
