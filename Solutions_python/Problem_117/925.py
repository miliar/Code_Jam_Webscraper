T = input()

for t in range(T):
    N, M = [int(x) for x in raw_input().split()]

    lawn = []
    grass_height = []
    for n in range(N):
        row = [int(x) for x in raw_input().split()]
        for height in row:
            if height not in grass_height:
                grass_height.append(height)
        lawn.append(row)
    grass_height.sort()

    answer = "YES"
    for i, height in enumerate(grass_height):
        for n in range(N):
            for m in range(M):
                if height == lawn[n][m]:
                    row = lawn[n]
                    column = [lawn[j][m] for j in range(N)]
                    if not all(row_height == height for row_height in row) and not all(column_height == height for column_height in column):
                        answer = "NO"

        if i+1 != len(grass_height):
            lawn = [[x if x > height else grass_height[i+1] for x in row] for row in lawn]

    print "Case #%d: %s" % (t+1, answer)
