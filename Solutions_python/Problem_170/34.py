import sys

str_to_id = {}

def get_id(s):
    if s in str_to_id:
        return str_to_id[s]
    str_to_id[s] = len(str_to_id)
    return str_to_id[s]

tn = int(sys.stdin.readline())
for test in xrange(tn, tn + 1):
    n = int(sys.stdin.readline())
    t = []
    for _ in xrange(n):
        t.append(sys.stdin.readline().strip().split())
    s = []
    for l in t:
        s.append(map(get_id, l))
    m = n - 2
    if m == 0:
        print "Case #{0}: {1}".format(test, len(set(s[0]) & set(s[1])))
    else:
        ans = 1000000000
        for mask in xrange(1 << m):
            eng = []
            fre = []
            for i in xrange(m):
                if (mask & (1 << i)) == 0:
                    eng.extend(s[i + 2])
                else:
                    fre.extend(s[i + 2])
            eng.extend(s[0])
            fre.extend(s[1])
            ans = min(ans, len(set(eng) & set(fre)))
        print "Case #{0}: {1}".format(test, ans)

