import sys

ncases = int(sys.stdin.readline())
for case in xrange(1,ncases+1):
    line = sys.stdin.readline().rstrip().split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    ans = 0.0
    nmachines = 0
    rate = 2.0
    if x <= c:
        print("Case #%d: %.7f" % (case, x/rate))
        continue
    to_x_no_add = x / rate
    to_f = c / rate
    to_x_add = to_f + x / (rate + f*(nmachines + 1))
    #print to_x_no_add, to_x_add
    while to_x_add < to_x_no_add:
        to_x_no_add = to_x_add
        rate += f
        to_f += c/rate
        to_x_add = to_f + x / (rate + f)
        #print to_x_no_add, to_f, to_x_add
    print("Case #%d: %.7f" % (case, to_x_no_add))

