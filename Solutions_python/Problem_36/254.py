import psyco
psyco.full()

def count(s, T, memo):
    x = len(s), len(T)
    if x in memo:
        return memo[x]

    if T == '':
        return 1

    if s == '':
        return 0


    cnt = 0
    if s[0] == T[0]:
        cnt += count(s[1:], T[1:], memo)
    cnt += count(s[1:], T, memo)

    memo[x] = cnt
    return cnt

def solve():
    T = 'welcome to code jam'
    for case in xrange(input()):
        s = raw_input()
        res = count(s, T, {})
        res = '%04d' % (res % 1000)
        print 'Case #%d: %s' % (case+1, res)

solve() # so that psyco can do its magic
