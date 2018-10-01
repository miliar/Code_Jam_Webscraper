import numpy as np

def row(fn):
    return map(fn, raw_input().strip().split())

for t in xrange(input()):
    R, C = row(int)
    pr = np.array([list(raw_input()) for _ in xrange(R)])
    letters = [(r,c) for r in xrange(R) for c in xrange(C) if pr[r][c] != '?']
    for r, c in letters:
        left = right = c
        up = down = r

        while left > 0:
            if pr[r,left-1] == '?': left -= 1
            else: break

        while right < C-1:
            if pr[r,right+1] == '?': right += 1
            else: break

        while up > 0:
            if set(pr[up-1,left:right+1]) == {'?'}: up -= 1
            else: break

        while down < R-1:
            if set(pr[down+1,left:right+1]) == {'?'}: down += 1
            else: break

        pr[up:down+1,left:right+1] = pr[r,c]


    assert '?' not in pr
    print 'Case #%d:' % (t+1)
    for r in pr:
        print ''.join(map(str, r))
