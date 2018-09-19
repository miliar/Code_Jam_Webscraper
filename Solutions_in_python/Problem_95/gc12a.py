A = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"] 
B = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

ma = dict()
for x in xrange(3):
    for y in xrange(len(A[x])):
        ma[A[x][y]] = B[x][y]
y = set("abcdefghijklmnopqrstuvwxyz")- set(ma.values())
ma['z']='q'
ma['q']='z'

with open('input.txt','r') as inf:
    out = open('output.txt','w')
    T = int(inf.readline())
    for case in xrange(1,T+1):
        cur = inf.readline()
        cur = cur.split('\n')[0]
        output = [ma[x] for x in cur]
        out.write("Case #%d: %s\n"%(case,''.join(output)))
    out.close()
