import sys

sys.stdin = open("input.in")
sys.stdout = open("output.txt", "w")
tn = int(sys.stdin.readline());

for ti in range(tn):
    [c, f, x] = [float(x) for x in sys.stdin.readline().split()];
    res = 0
    gr = 2
    roi = c / f
    est = x / gr
    while est > roi + c/gr:
        res += c/gr
        gr += f
        est = x / gr

    res += est
    print "Case #%s:" % (ti + 1), res

sys.stdout.close()
