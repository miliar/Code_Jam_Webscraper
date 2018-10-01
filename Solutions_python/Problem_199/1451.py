def flip(s, start, K):
    if start+K > len(s):
        return s
    s2 = list(s[:start])
    for i in range(start, start+K):
        s2.append('-' if s[i] == '+' else '+')
    s2.append(s[start+K:])
    return "".join(i for i in s2)

def solve(s, K):
    flip_count = 0
    for i in range(len(s)-K+1):
        if not(s[i] == '+'):
            s = flip(s, i, K)
            flip_count += 1
    if '-' in s: return 'IMPOSSIBLE'
    return flip_count

t = int(raw_input())
for i in xrange(1, t+1):
    s, K = raw_input().split(" ")
    K = int(K)
    print "Case #{}: {}".format(i, solve(s, K))