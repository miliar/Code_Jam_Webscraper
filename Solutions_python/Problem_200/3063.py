def findTidy(l):
    for upper in range(len(l), -1, -1):
        i = upper - 1
        if upper == 0:
            return l

        if max(l[:upper]) != l[i]:
            if i - 1 >= 0:
                l[i-1] -= 1
                for j in range(i, len(l)):
                    l[j] = 9
            if i == 1 and l[i-1] <= 0:
                l.pop(i-1)
    return l

cases = int(raw_input())
for case in range(1, cases + 1):
    n = map(int, list(raw_input().strip()))
    l = findTidy(n)
    val = ''.join(map(str, l))
    print('Case #%d: %s' % (case, val))
