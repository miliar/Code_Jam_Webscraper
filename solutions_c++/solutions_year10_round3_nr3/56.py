#!/usr/bin/python

inf = open("input.txt")
ouf = open("input2.txt",'w')
read = inf.readline
out = ouf.write

t = int(read())
out("%d\n"%t)

to={}
to['0']='0 0 0 0 '
to['1']='0 0 0 1 '
to['2']='0 0 1 0 '
to['3']='0 0 1 1 '
to['4']='0 1 0 0 '
to['5']='0 1 0 1 '
to['6']='0 1 1 0 '
to['7']='0 1 1 1 '
to['8']='1 0 0 0 '
to['9']='1 0 0 1 '
to['A']='1 0 1 0 '
to['B']='1 0 1 1 '
to['C']='1 1 0 0 '
to['D']='1 1 0 1 '
to['E']='1 1 1 0 '
to['F']='1 1 1 1 '

for test in range(t):
    m,n=map(int,read().split())
    out("%d %d\n"%(m,n))
    for i in range(m):
        s = read().strip()
        s2 = ""
        for j in s:
            s2 += to[j]
        out("%s\n"%s2)
