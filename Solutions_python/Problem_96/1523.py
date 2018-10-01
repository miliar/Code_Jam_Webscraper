sources=['ejp mysljylc kd kxveddknmc re jsicpdrysi',
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
'de kr kd eoya kw aej tysr re ujdr lkgc jv',
'y qee',
'z']
targets=['our language is impossible to understand',
'there are twenty six factorial possibilities',
'so it is okay if you want to just give up',
'a zoo',
'q']
dictionary={}
f = open('A-small-attempt0.in','r')
g = open('A.out','w')
for source,target in zip(sources,targets):
    #print source
    #print target
    #source = 'abc'
    #target = 'def'
    for s,t in zip(source, target):
        dictionary[s] = t

T=int(f.readline().strip())
for i in range(T):
    line = f.readline().strip()
    #print line
    i=i+1
    Aline="Case #"+str(i)+": "
    for letter in line:
        Aline=Aline+dictionary[letter]
    print >>g, Aline
