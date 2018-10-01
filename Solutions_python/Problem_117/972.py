def test(lawn, n, m, nCase):
    rMax = [0 for i in range(n)]
    cMax = [0 for j in range(m)]
    for i in range(n):
        for j in range(m):
            if lawn[i][j] > rMax[i]:
                rMax[i] = lawn[i][j]
            if lawn[i][j] > cMax[j]:
                cMax[j] = lawn[i][j]
    print 'Case #' + str(nCase) + ':',
    for i in range(n):
        for j in range(m):
            if rMax[i] > lawn[i][j] and cMax[j] > lawn[i][j]:
                print 'NO'
                return
    print 'YES'

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        strLine = raw_input().split(' ')
        n, m = int(strLine[0]), int(strLine[1])
        test([[int(num) for num in raw_input().split(' ')] for j in range(n)], n, m, i + 1)

