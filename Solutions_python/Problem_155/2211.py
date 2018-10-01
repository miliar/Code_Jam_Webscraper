__author__ = 'Emperor'
cases = int(input())
for case in range(1, 1 + cases):
    s, detail = [x for x in input().split()]
    ans = 0
    total = 0
    for i in range(int(s) + 1):
        if i > total:
            diff = i - total
            ans += diff
            total += diff
        total += int(detail[i])
    print('Case #%d: %d' % (case, ans))
