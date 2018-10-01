import sys
import time

with open(sys.argv[1]) as file:
    t = int(file.readline())
    for n in range(1,t+1):
        c,f,x = map(float,file.readline().split())
        r = 2
        total = 0.0
        while x > 0:
#             print c,f,x
#             time.sleep(1)
            if (c/r + x/(r+f)) < x/r :
                total += c/r
                r += f
            else:
                total += x/r
                break
        print "Case #%d: %.7f" % (n,total)