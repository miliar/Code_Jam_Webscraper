import sys


def solve(N):
    nthDigitsDecreasing = len(N)
    firstDigitsSame = 0

    for i in range(len(N)-1):
        if N[i] < N[i+1]:
            firstDigitsSame = i+1
        elif N[i] > N[i+1]:
            nthDigitsDecreasing = firstDigitsSame
            break
    for i in range(len(N)):
        if i == nthDigitsDecreasing:
            N[i] -= 1
        elif i > nthDigitsDecreasing:
            N[i] = 9

    return ''.join(map(str, N)).lstrip('0')


T = int(input())
for i in range(T):
    N = list(map(int, input()))
    print('Case #{}: {}'.format(i+1, solve(N)))