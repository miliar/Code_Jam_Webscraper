
import sys

ntests = int(sys.stdin.readline())

for ncase in range(ntests):
    chars, K = sys.stdin.readline().split(' ')
    K = int(K)
    chars = list(chars)

    isOk = True
    count = 0

    for i, c in enumerate(chars):
        if chars[i] == '+':
            continue

        if i + K > len(chars):
            isOk = False
            break

        count += 1

        for j in range(K):
            chars[i + j] = '-' if chars[i + j] == '+' else '+'


    if not isOk:
        result = "IMPOSSIBLE"
    else:
        result = count

    print('Case #{0}: {1}'.format(ncase + 1, result))
