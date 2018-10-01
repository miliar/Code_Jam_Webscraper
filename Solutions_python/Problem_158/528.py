def solve():
    x, r, c = map(int, input().split())
    if r > c:
        r, c = c, r
    richard = True
    if x == 1:
        richard = False
    # if x > c or c * r % x != 0:
    #     richard = True
    if x == 2 and r == 1 and c == 2:
        richard = False
    if x == 2 and r == 1 and c == 4:
        richard = False
    if x == 2 and r == 2 and c == 2:
        richard = False
    if x == 2 and r == 2 and c == 3:
        richard = False
    if x == 2 and r == 2 and c == 4:
        richard = False
    if x == 2 and r == 3 and c == 4:
        richard = False
    if x == 2 and r == 4 and c == 4:
        richard = False
    if x == 3 and r == 1 and c == 3:
        richard = True
    if x == 3 and r == 2 and c == 3:
        richard = False
    if x == 3 and r == 3 and c == 3:
        richard = False
    if x == 3 and r == 3 and c == 4:
        richard = False
    if x == 4 and r == 1 and c == 4:
        richard = True
    if x == 4 and r == 2 and c == 4:
        richard = True
    if x == 4 and r == 3 and c == 4:
        richard = False
    if x == 4 and r == 4 and c == 4:
        richard = False
    return 'RICHARD' if richard else 'GABRIEL'

T = int(input())
for t in range(T):
    print('Case #{}: '.format(t + 1), end='')
    ans = solve()
    print(ans)
