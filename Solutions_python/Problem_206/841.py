def work():
    d, n = map(int, input().split())
    xvs = [tuple(map(int, input().split())) for _ in range(n)]
    return d / max((d - xv[0]) / xv[1] for xv in xvs)


for i in range(int(input())):
    print('Case #{}: {:.7f}'.format(i + 1, work()))
