t = int(raw_input())

for k in range(t):
    c,f,x = [float(e) for e in raw_input().split(" ")]

    rate = 2.0
    ct = 0.0

    while True:
        #print "ct "+str(ct)
        #print "rate "+str(rate)
        next_time = c/rate
        win_building = next_time + x/(rate+f)
        win_without = x/rate
        #print "win build "+str(win_building)
        #print "win no build"+str(win_without)
        if win_without <= win_building:
            best_time = win_without + ct
            break
        else:
            ct += next_time
            rate += f

    print "Case #{0}: {1:.7f}".format(k+1,best_time)

