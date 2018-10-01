#!/usr/bin/env python

f = open("b.in", "r")
fout = open("b.out", "w")

data = f.readlines()

#print data
#print int(data[0])

def normal(i):
    if i % 3 == 0: return i/3
    if i % 3 == 1: return i/3+1
    if i % 3 == 2: return i/3+1

def surprise(i):
    if i == 0: return 0
    if i == 1: return 1
    if i == 29: return 10
    if i == 30: return 10
    return (i-2)/3+2 # empyric

for i in range (1, int(data[0])+1):
    l = data[i].rstrip('\n')
#    print l
    s = l.split(" ")

    st = int(s[1]) # surprising triplet
    p = int(s[2])
    y = 0 # result

    for j in range(3,int(s[0])+3):
        n = int(s[j])
        print n, normal(n), surprise(n)
        if normal(n) >= p : # already OK
            y += 1
#            print "OK"
        elif surprise(n) >= p and st > 0: # OK if surprise
            y += 1
            st -= 1
#            print "OK surprise"

#    print s
    res = "Case #{0}: {1}\n".format(i, y)
    print res.rstrip()
    fout.write(res)

