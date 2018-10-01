from sys import stdin as st
from math import floor

t = int(st.readline())

for case in xrange(1, t + 1):

    a, b =  st.readline().split()
    ai = int(a)
    bi = int(b)


    count = 0

    for i in xrange(ai, bi + 1):

        sqi = i ** (0.5)
        i_str = str(i)
        ilen = len(i_str) 
        sqi_str = str(int(floor(sqi)))
        sqilen = len(sqi_str)
        
        if (floor(sqi) ** 2) != i:
            continue 


        if ilen & 1:
            if i_str[:(ilen/2)] != i_str[(ilen/2) + 1:]:
                continue
        else:
            if i_str[:(ilen/2)] != i_str[(ilen/2):]:
                continue


        if sqilen & 1:
            if sqi_str[:(sqilen/2)] != sqi_str[(sqilen/2) + 1:]:
                continue
        else:
            if sqi_str[:(sqilen/2)] != sqi_str[(sqilen/2):]:
                continue

        count += 1

    print "Case #%d: %d" % (case, count)






