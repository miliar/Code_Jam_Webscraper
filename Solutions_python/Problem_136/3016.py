T = int(raw_input())
for I in range(1, T+1):
    C, F, X = raw_input().split(" ")
    C, F, X = float(C), float(F), float(X)
    curr_rate = 2
    time = 0
    while C / curr_rate + X / (curr_rate + F) < X / curr_rate:
        time += C / curr_rate
        curr_rate += F
    time += X / curr_rate
    print("Case #%d: %.7f" % (I, time))