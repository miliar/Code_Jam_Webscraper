import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    N, M = map(int, f.readline().split())
    rows = [map(int, f.readline().split()) for row in range(N)]
    columns = [[rows[i][j] for i in range(N)] for j in range(M)]

    answer = 'YES'
    for i in range(N):
        for j in range(M):
            height = rows[i][j]
            if height < max(rows[i]) and height < max(columns[j]):
                answer = 'NO'
    
    print "Case #%d:" % (t + 1), answer
