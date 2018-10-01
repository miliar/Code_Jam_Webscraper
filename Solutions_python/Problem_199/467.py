t = int(raw_input())
for a in xrange(t):
    [state, m] = raw_input().split(' ')
    m = int(m)
    state = [True if i == '+' else False for i in state]
    res = 0
    for i in xrange(len(state)-m):
        s = state[i]
        if s == False:
            res += 1
            for j in xrange(m):
                state[j+i] = not state[j+i]
    f = state[-m]
    for s in state[-m+1:]:
        if s != f:
            print 'Case #%d: IMPOSSIBLE' % (a+1)
            break
    else:
        if f == False: res += 1
        assert reduce(lambda i, j: i and j, state[:-m], True)
        print 'Case #%d: %d' % (a+1, res)
    