import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for t in range(T):
    C, F, X = [float(x) for x in f.readline().split()]
    rate = 2

    time = 0
    while True:
        time_at_current_rate = X / rate
        time_with_new_farm = (C / rate) + (X / (rate + F))
        if time_at_current_rate <= time_with_new_farm:
            time += time_at_current_rate
            break
        else:
            time += (C / rate)
            rate += F
     
    print "Case #%d: %0.6f" % ((t + 1), time)
