def calc_lowest_score(r, c, w):
    ans = c // w
    if c % w > 0:
        ans += w
    else:
        ans += w - 1
    return ans

for case in range(int(input())):
    ans = calc_lowest_score(*[int(x) for x in input().split()])
    print("Case #{0}: {1}".format(case+1, ans))