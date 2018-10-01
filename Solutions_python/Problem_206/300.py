def solve(ip,d,n):
    res = 0

    max_t = 0

    for k,s in ip:
        t = (d-k) / s
        if t > max_t :
            max_t = t



    return d/max_t


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        d,n = map(int,input().strip().split())
        ip = []
        for ni in range(n):
            ip.append(list(map(int,input().strip().split())))
        res = solve(ip,d,n)
        print("Case #{}: {:.6f}".format(ti + 1, res))
