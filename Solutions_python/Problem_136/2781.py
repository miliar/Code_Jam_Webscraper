import sys
sys.stdin = open('B-large.in')
sys.stdout = open('B-large.out', 'w')


for t in range(1, input()+1):
    inline = raw_input().strip().split(' ')
    C, F, X = float(inline[0]), float(inline[1]), float(inline[2])

    def s(current, mintime, timeuntilnow):
        while True:
            eta = X/current
            tbuy = C/current

            if mintime < timeuntilnow + eta and mintime < timeuntilnow + tbuy:
                return mintime

            if eta < tbuy:
                return timeuntilnow + eta
            else:
                new_current = current+F
                new_timeuntilnow = timeuntilnow+tbuy
                if timeuntilnow + eta < mintime:
                    new_mintime = timeuntilnow+eta
                else:
                    new_mintime = mintime

                current = new_current
                timeuntilnow = new_timeuntilnow
                mintime = new_mintime
    print 'Case #' + str(t) + ':', s(2, float("inf"), 0)
