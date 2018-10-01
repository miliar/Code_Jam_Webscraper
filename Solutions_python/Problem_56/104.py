step = (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)

t = int(raw_input())
for i in range(t):
    n, k = [int(s) for s in raw_input().split()]
    b = ['.' * (n + 2 * k)] * k
    for j in range(n):
        r = raw_input().replace('.', '')
        b.append('.' * (k + n - len(r)) + r + '.' * k)
    for j in range(k):
        b.append('.' * (n + 2 * k))

    found = { 'R': False, 'B' : False }
    total = { 'R': [[[0] * 8] * (n + 2)] * (n + 2),
              'B': [[[0] * 8] * (n + 2)] * (n + 2) }
    for y in range(k, k + n):
        for x in range(k, k + n):
            c = b[x][y]
            if c is not '.' and not found[c]:
                for d in range(8):
                    xx = x - k + 1
                    yy = y - k + 1
                    total[c][xx][yy][d] = 1
                    if d is 0 or d is 6 or d is 7 and \
                        total[c][xx + step[d][0]][yy + step[d][1]][d] > 0:
                        total[c][xx][yy][d] += \
                            total[c][xx + step[d][0]][yy + step[d][1]][d]
                    else:
                        for j in range(1, k):
                            if b[x + step[d][0] * j][y + step[d][1] * j] is c:
                                total[c][xx][yy][d] += 1
                            else:
                                break
                    if total[c][xx][yy][d] is k: 
                        found[c] = True
                        break
    if found['R'] and found['B']:
        result = 'Both'
    elif found['R']:
        result = 'Red'
    elif found['B']:
        result = 'Blue'
    else:
        result = 'Neither'
    print 'Case #{0}: {1}'.format(i + 1, result)
