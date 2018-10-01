import sys

f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    N, M = [int(v) for v in f.readline().split()]
    field = []
    c_max = []
    r_max = []
    for i in range(N):
        row = [int(v) for v in f.readline().split()]
        field.append(row)
        r_max.append(max(row))
    for i in range(M):
        column = []
        for row in field:
            column.append(row[i])
        c_max.append(max(column))
    status = 'YES'
    for i in range(N):
        for j in range(M):
            if field[i][j] < r_max[i] and field[i][j] < c_max[j]:
                status = 'NO'
                break
        if status == 'NO':
            break

    print 'Case #%s: %s' % (t+1, status)
