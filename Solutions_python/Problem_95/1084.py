#/usr/bin/python

a="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

b="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

D={}

i=0
while i<len(a):
    D[a[i]]=b[i]
    i+=1

D['z']='q'
D['q']='z'


import sys
wt=sys.stdout.write
f=open('a1.dat')
NUM=int(f.readline())
i=0

while i<NUM:
    i+=1
    wt('Case #%d: '%i)
    for c in f.readline():
        #if not D.has_key(c):wt('<'+c+'>')
        wt(D[c])
