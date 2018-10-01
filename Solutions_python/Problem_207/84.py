total_case = input()
for test_case in xrange(1, total_case + 1):
    n, r, o, y, g, b, v = map(int, raw_input().split())
    a = sorted([(r, 'R'), (y, 'Y'), (b, 'B')])[::-1]
    #print a
    if (a[0][0] > a[1][0] + a[2][0]):
        print 'Case #' + str(test_case) + ': ' + 'IMPOSSIBLE'
    else:
        ans = ['x'] * n
        for i in xrange(a[0][0]):
            ans[i * 2] = a[0][1]
        a = sorted(a[1:])[::-1]
        for i in xrange(n):
            if ans[i] == 'x':
                ans[i] = a[0][1]
                a[0] = (a[0][0] - 1, a[0][1])
                assert(a[0][0] >= 0)
                a = sorted(a)[::-1]
        print 'Case #' + str(test_case) + ': ' + ''.join(ans)
        
