import sys

getl = lambda : sys.stdin.readline().strip()

cases = range(int(getl()))
for case in cases:
    N,M = [int(x) for x in getl().split()]
    result = 'YES'
    heights = []
    for i in range(N):
        heights.append(tuple(int(x) for x in getl().split()))

    coheights = list(zip(*heights))

    for row in range(1,N-1):
        for col in range(1,M-1):
            patch = heights[row][col]
            if max(heights[row]) > patch and max(coheights[col]) > patch:
                result = 'NO'
                break

    if result == 'YES' and N > 1:
        for row in (0,N-1):
            for col in range(M):
                patch = heights[row][col]
                if max(heights[row]) > patch and max(coheights[col]) > patch:
                    result = 'NO'
                    break

    if result == 'YES' and M > 1:
        for col in (0,M-1):
            for row in range(1,N-1):
                patch = heights[row][col]
                if max(heights[row]) > patch and max(coheights[col]) > patch:
                    result = 'NO'
                    break

    if M == 1 and N == 1:
        result = 'YES'

    print('Case #{0}: {1}'.format(case+1, result))
