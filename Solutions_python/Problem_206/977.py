T = int(input().strip())

for x in range(1, T+1):
    d, n = list(map(int,input().strip().split(' ')))
    mt = 0
    for h in range(n):
        pos, speed = list(map(int,input().strip().split(' ')))
        if ((d-pos) / speed) > mt:
            mt = (d-pos) / speed
    print("Case #{}: {}".format(x,d/mt))
