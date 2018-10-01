import sys

tc = int(sys.stdin.readline().strip())

for i in range(tc):
    c, f, x = [float(v.strip()) for v in sys.stdin.readline().strip().split()]
    best = x / 2

    time = 0
    rate = 2
    j = 0
    while True:
        j += 1
        time += c / rate
        rate += f
        if time + x / rate < best:
            best = time + x / rate
        else:
            break

    print("Case #%d: %0.7f" % (i+1, best))
