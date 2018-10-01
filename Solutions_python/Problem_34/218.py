import re

L, D, N = [int(x) for x in raw_input().strip().split()]
#print L, D, N

dic = []
for i in range(D):
    dic.append(raw_input().strip())
#print dic

for i in range(N):
    pat = raw_input().strip()
    pat = pat.replace("(", "[").replace(")", "]")
    #print "%s" % pat
    matcher = re.compile(pat)

    count = 0
    for word in dic:
        if matcher.match(word):
            count += 1

    print "Case #%d: %d" % (i+1, count)

