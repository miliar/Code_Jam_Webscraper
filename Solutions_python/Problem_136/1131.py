T = input()

for casenbr in range(T):
    C, F, X = [float(i) for i in raw_input().strip().split()]
    t = [C/(2+n*F) for n in range(100000)]
    tau = [X/(2+n*F) for n in range(100000)]

    idx = 0
    while 1:
        if t[idx] + tau[idx+1] > tau[idx]:
            break
        idx += 1
    ans = sum(t[:idx]) + tau[idx]

    print "Case #%d: %.7f" % (casenbr+1, ans)
