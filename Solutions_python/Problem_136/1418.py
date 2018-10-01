from codejam import *

for i in xrange(readint()):
    C, F, X = readfloatarray()
    initial_time = 0.0

    cookies_per_sec = 2.0
    while True:
        t = initial_time + C / cookies_per_sec + X / (F + cookies_per_sec)
        if t < initial_time + (X / cookies_per_sec):
            initial_time += C / cookies_per_sec
            cookies_per_sec += F
        else:
            t = initial_time + (X / cookies_per_sec)
            break
    
    print "Case #%d: %.7f" % (i + 1, t)
