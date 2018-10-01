#! /usr/bin/python

inp = open("in")

inp.readline()
i = 1
for line in inp:
    print "Case #" + str(i) + ":",
    line = line.split()
    (N, S, p) = map(int, line[0:3])
    nbsurprises = 0
    ok = 0
    for googler in map(int, line[3:]):
        val = (googler - p) / 2
        if val >= 0:
            if val == p - 2:
                nbsurprises += 1
            elif val > p - 2:
                ok += 1
    print ok + min(nbsurprises, S)
    i += 1
