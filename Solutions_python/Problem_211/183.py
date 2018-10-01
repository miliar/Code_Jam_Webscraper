
def calc(opt):
    ans = 1.0
    for l in opt:
        ans *= l
    return ans

t = int(raw_input())

for case in range(t):

    n, k = [int(o) for o in raw_input().split()]
    s = float(raw_input())

    opt = [float(o) for o in raw_input().split()]

    tmp = s

    while tmp > 0.0000001:
        opt.sort()
        j = min(opt)
        num = 0
        minus = 0.0
        for i in opt:
            if i == j:
                num += 1
            else:
                minus = i - j
                break
        if minus == 0:
            minus = 1.0 - j
        if tmp >= minus * num:
            for i in range(n):
                if opt[i] == j:
                    opt[i] += minus
                else:
                    break
            tmp -= minus * num
        else:
            for i in range(n):
                if opt[i] == j:
                    opt[i] += tmp / num
                else:
                    break
            tmp = 0

    print "Case #%d: %.6f" % (case + 1, calc(opt))

