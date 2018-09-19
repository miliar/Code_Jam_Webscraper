cc = '<v>^'
qq = {'<':(0, -1), '>':(0, 1), 'v':(1, 0), '^':(-1, 0)}
r, c = 0, 0
s = list([])

def go(i, j):
    dx, dy = qq[s[i][j]]
    while 1:
        i += dx
        j += dy
        if i<0 or j<0 or i>=r or j>=c:
            return False
        if s[i][j] in cc or s[i][j] == '#':
            return True
    return False

def gogo():
    ans = 0
    for i in range(r):
        for j in range(c):
            if s[i][j] in cc:
                if go(i, j):
                    s[i][j] = '#'
                else:
                    q = ans
                    for k in cc:
                        s[i][j] = k
                        if(go(i, j)):
                            s[i][j] = '#'
                            ans += 1
                            break
                    if ans == q:
                        return -1
    return ans


for t in range(input()):
    r, c = map(int, raw_input().split())
    s = list(list(raw_input()) for i in range(r))
    ans = gogo()
    if ans < 0:
        print 'Case #%d: IMPOSSIBLE' % (t+1)
    else:
        print 'Case #%d: %d' % (t+1, ans)

