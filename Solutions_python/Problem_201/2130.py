def simulate(n, k):
    if k == 1:
        return n-1
    elif not k%2:
        return simulate(int(n / 2), int(k / 2))
    elif not n%2:
        return simulate(int(n/2-1), int(k/2))
    else:
        return simulate(int(n / 2), int(k / 2))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = map(int, input().split())
    r = simulate(n, k)
    if r%2:
        max_ = int((r+1)/2)
        min_ = int((r-1)/2)
    else:
        max_ = int(r/2)
        min_ = int(r / 2)
    print("Case #{}: {} {}".format(i, max_, min_))


