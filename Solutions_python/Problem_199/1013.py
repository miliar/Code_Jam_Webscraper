N = input()

for i in range(N):
    line, K = raw_input().split()
    line, K = list(line), int(K)

    count = 0

    for j in range(len(line) - K + 1):
        if line[j] == '-':
            for k in range(K):
                if line[j + k] == '-':
                    line[j + k] = '+'
                elif line[j + k] == '+':
                    line[j + k] = '-'
            count += 1

    if '-' in line:
        print 'Case #%d: IMPOSSIBLE' % (i + 1)
    else:
        print 'Case #%d: %d' % (i + 1, count)
