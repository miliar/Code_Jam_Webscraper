def flip(s, i, k):
    sub = s[i:i + k]
    tmp = ''
    for c in sub:
        if c == '+':
            tmp += '-'
        else:
            tmp += '+'
    return s[:i] + tmp + s[i + k:]


def solve(s, k):
    moves = 0
    q = []
    q.append(s)
    visited = {s: True}
    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            top = q.pop(0)
            if '-' not in top:
                return moves
            for i in range(0, len(top) - k + 1):
                new_s = flip(top, i, k)
                if new_s not in visited:
                    q.append(new_s)
                    visited[new_s] = True
        moves += 1
    return 'IMPOSSIBLE'


t = int(raw_input())
for i in range(t):
    s, k = raw_input().split()
    k = int(k)
    print "Case #%d: %s" % (i + 1, solve(s, k))
