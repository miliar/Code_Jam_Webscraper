import sys

f = open('code.txt')

d = dict([line.split() for line in f])
d.update({' ':' '})

T = int(raw_input())

for Ti in range(1,T+1):
    print "Case #%d:" % (Ti),
    line = raw_input()
    s = ""
    for i in range(len(line)):
        s = s + d[line[i]]
    print s

