ncase = int(raw_input())
for i in range(0, ncase):
    n, m = raw_input().split(' ')
    m = m.rstrip('0')
    sum, ans = 0, 0
    for idx, obj in enumerate(list(m)):
        if sum < idx:
            ans += idx-sum
            sum = idx
        sum += int(obj)
    print 'Case #%s: %s' % (i+1, ans)