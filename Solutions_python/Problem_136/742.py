def test(C, F, X):
    time = 0
    speed = 2.0
    best = float("inf")
    final = 0
    it = 0

    while True:
        final = time + X / speed
        #print(best, final, time, speed, C, F, X)

        if final < best:
            best = final

            time += C / speed
            speed += F
        else:
            break

    return best

with open("B-large.in", "r") as f:
    with open("B-large.out", "w") as fo:
        line = f.readline()

        T = int(line.strip())

        for i in range(T):
            C, F, X = list(map(float, f.readline().strip().split()))
            result = test(C, F, X)
            print("%.7f" % result)
            fo.write('Case #%d: %.7f\n' % (i+1, result))
            