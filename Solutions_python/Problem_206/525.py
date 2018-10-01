import sys

stdout = sys.stdout
stdin = sys.stdin
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def solve():
    result = 0
    D, N = map(int, input().split())
    maxTime = 0
    for i in range(N):
        k, s = map(int, input().split())
        time = (D-k)/s
        if (time > maxTime):
            maxTime = time
    result = D/maxTime
    return result

T = int(input())
for CASE in range(1,T+1):
    print('Case #' + str(CASE) + ': ', end='')
    print(solve())

sys.stdout = stdout
sys.stdin = stdin
