source = "D-small-attempt0"
sin = source+".in"
sout = source+".out"

#http://snippets.dzone.com/posts/show/753
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def perm(x, p):
    n = ""
    l = len(p)
    for part in xrange(l, len(x)+1, l):
        spec = x[part-l:part]
        for c in xrange(l):
            n += spec[p[c]-1]
    return n

def killre(x):
    n = ""
    for i in xrange(len(x)):
        if i == 0 or x[i] != x[i-1]:
            n += x[i]
    return n

txt = open(sin).readlines()
txt = [x.strip() for x in txt]

txt.pop(0)

cases = []
while txt:
    cases.append( (int(txt.pop(0)), txt.pop(0)) )

f = open(sout, "w")

for num, (k, s) in enumerate(cases):
    best = len(s)
    for i in [k+1]:
        if len(s)%(i-1) == 0:
            for p in all_perms( range(i)[1:] ):
                l = len(killre(perm(s, p)))
                if l < best:
                    print perm(s,p), p
                    best = l
    answer = "Case #%d: %d" % (num+1, best)
    print answer
    f.write(answer+"\n")
f.close()
