from collections import defaultdict

xor = lambda l: reduce(lambda a,b:a^b, l)

def solve(p, s, mem, result):
    for i in xrange(len(p)):
        p2 = p[:]
        e = p2.pop(i)
        s2 = s[:]
        s2.append(e)
        s2.sort()

        k = tuple(p2 + [None] + s2)
        if k not in mem:
            solve(p2, s2, mem, result)
            mem[k] = True
            if p2 and s2 and xor(s2) == xor(p2):
                result.append(sum(s2))


for case in xrange(input()):
    N = input()
    candies = map(int, raw_input().split())

    r = []
    solve(sorted(candies), [], defaultdict(set), r)
    if not r:
        print "Case #%i: NO" % (case+1,)
    else:
        print "Case #%i: %i" % (case+1, max(r))
