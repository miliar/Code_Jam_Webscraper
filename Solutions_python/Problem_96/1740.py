from math import *
t = input()

for i in range(1, t+1):
    s = str(raw_input())
    s = s.split()
    s = map(int, s)
    N = s[0]
    S = s[1]
    p = s[2]
    s = s[3::]
    r = 0
    for j in s:
        if (j >= ((p * 3) - 2)):
            r += 1
        elif ((2 <= j <= 28 ) and j >= 3 * p - 4 and S > 0):
            r += 1
            S -= 1
        
    print "Case #" + str(i) + ": " + str(r)
    #print s
    #print str(N)  + "=" + str(S) + "=" + str(p)
