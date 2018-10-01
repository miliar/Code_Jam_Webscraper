def solve():
    d = [float(j) for j in raw_input().split()]
    pps = 2.0   # production per second
    time_consumed = 0.0   # time already spent
    while True:
        time = d[2]/pps
        time_if_buy = d[0]/pps + d[2]/(pps+d[1])
        if time > time_if_buy:
            time_consumed += d[0]/pps
            pps += d[1]
        else:
            break
    return time_consumed + time

a = input()
for i in range(a):
    print "case #{0}: {1}".format(i+1, "%.8f" % solve())
