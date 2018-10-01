#input = list(open('in.txt'))[::-1].pop

def solve():
    D, N = map(int, input().split())
    maxtime = 0
    for _ in range(N):
        K, S = map(int, input().split())
        maxtime = max(maxtime, (D - K) / S)
    return D / maxtime

T = int(input())
for x in range(1, T+1):
    print('Case #{}: {}'.format(x, solve()))
