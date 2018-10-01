def uniq(w):
    l = [w[0]]
    for i in range(1, len(w)):
        if w[i] != l[-1]:
            l.append(w[i])
    return ''.join(l)

def counts(w):
    c = w[0]
    cpt = 0
    res = []
    for wi in w:
        if wi == c:
            cpt += 1
        else:
            res.append(cpt)
            cpt = 1
            c = wi
    res.append(cpt)
    return res

def solve(words):
    if len(set(uniq(w) for w in words)) != 1:
        return "Fegla Won"
    c = [counts(w) for w in words]
    r = 0
    for i in range(len(c[0])):
        mean = sum(ci[i] for ci in c) / len(words)
        t = 1000000000000000000
        for v in range(max(mean-5, 0), mean+5):
            t = min(t, sum(abs(ci[i]-v) for ci in c))
        r += t
    return r
    

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    sol = solve([raw_input().strip() for i in range(N)])
    print "Case #{}: {}".format(t+1, sol)
