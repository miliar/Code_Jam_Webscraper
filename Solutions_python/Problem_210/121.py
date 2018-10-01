T = int(input())
for case in range(1, T+1):
    ac, aj = map(int, input().split())
    tc = [list(map(int, input().split())) for _ in range(ac)]
    tj = [list(map(int, input().split())) for _ in range(aj)]
    tj.sort()
    tc.sort()
    if ac > aj:
        ac, aj = aj, ac
        tc, tj = tj, tc
    if [ac, aj] in ([0, 0], [0, 1], [1, 0], [1, 1]):
        result = 2
    elif ac == 0 and aj == 2:
        # print(tj)
        if (tj[1][0] - tj[0][1]) >= 24*30 or (tj[0][0] - tj[1][1]+24*60) >= 24*30:
            result = 2
        else:
            result = 4
    elif ac == 1 and aj == 2:
        if tj[0][1] <= tc[1][0] <= tj[1][0]:

            if (tj[1][0] - tj[0][1]) >= 24*30:
                result = 2
            else:
                result = 4
        elif (tj[0][0] - tj[1][1]+24*60) >= 24*30:
            reuslt = 2
        else:
            result = 4
        result = "?"
    elif ac == aj == 2:
        result = "?"
    print(f"Case #{case}: {result}")
