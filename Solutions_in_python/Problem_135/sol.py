def solve():
    r = int(input())
    fr = [list(map(int, input().split())) for i in range(4)][r-1]
    c = int(input())
    fc = [list(map(int, input().split())) for i in range(4)][c-1]
    ans = []
    for v in fr:
        if v in fc:
            ans.append(v)
    if len(ans) == 1:
        return ans[0]
    if len(ans) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

tst = int(input())
for i in range(tst):
    print("Case #" + str(i+1) + ": " + str(solve()))
