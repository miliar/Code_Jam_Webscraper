s1 = ["ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv","zq"]
s2 = ["our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up","qz"]
m = dict()

for i in range(len(s1)):
    for j in range(len(s1[i])):
        m[s1[i][j]] = s2[i][j]

f = open("inp1","r")
n = int(f.readline())
for i in range(1,n+1):
    print "Case #"+str(i)+":",
    s = f.readline().strip()
    ff = lambda x: m[x]
    print "".join(map(ff,s))
