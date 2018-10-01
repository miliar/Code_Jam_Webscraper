#! /usr/bin/python

associations = {}
ass = open("associations")
for line in ass:
    asso = line.strip('\n').split()
    associations[asso[1]] = asso[0]
associations[' '] = ' '
inp = open("in")
inp.readline()
i = 1
for line in inp:
    print "Case #" + str(i) + ":",
    res = ""
    for k in xrange(len(line) - 1):
        res += associations[line[k]]
    print res
    i += 1
