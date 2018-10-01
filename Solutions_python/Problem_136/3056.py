f = open('input.txt', 'r')

T = int(f.readline())
for case in range(T):
    total_time = 0
    C, F, X = map(float, f.readline().split())

    rate = 2
    while X > 0:
        if X >= C:
            step_time1 = X / rate
            upgrade_time = C / rate
            step_time2 = upgrade_time + X / (rate + F)
            if step_time2 < step_time1:
                total_time = total_time + upgrade_time
                rate = rate + F
            else:
                total_time = total_time + step_time1
                X = 0
        else:
            total_time = total_time + X / rate
            X = 0

    print("Case #{0}: {1:.7f}".format(case+1, total_time))

