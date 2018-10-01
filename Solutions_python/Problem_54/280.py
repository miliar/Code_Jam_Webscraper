def readData(t):
    res = []
    for i in t.split(" ")[1:]:
        res.append(int(i))
    return res

def unique(t):
    res = []
    for i in t:
        if i not in res:
            res.append(i)
    return res

def GCD(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

def GCDD(t):
    res = abs(t[1] - t[0])
    for i in range(0, len(t)):
        for j in range(i + 1, len(t)):
            res = GCD(res, abs(t[i] - t[j]))
    return res

def Check(t, y, T):
    for i in t:
        if (i + y) % T != 0:
            return False
    return True

def work(t):
    t.sort()
    t = unique(t)
    T = GCDD(t)
    k = ((t[-1] - 1) / T + 1) * T
    while not Check(t, k - t[-1], T):
        k += T
    return k - t[-1]

def main():
    f = open("b.in", "rt")
    t = int(f.readline())
    for i in range(1, t + 1):
        res = work(readData(f.readline()))
        print "Case #%d: %d" % (i, res)

main()

