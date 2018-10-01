"""
find the value for quotient_score % 3 from the below table and
add it to the quotient of total_score/3 to get the best result 
remainder  surprising normal
    0           +1      +0
    1           +1      +1
    2 	        +2      +1
"""

d = {   0   : (0, 1),
        1   : (1, 1),
        2   : (1, 2)    }


def is_ge_p(n, s, p, tot_pt):
    tmp = tot_pt / 3
    remainder = tot_pt % 3
    if tmp + d[remainder][0] >= p:
        return (True, s)
    elif tmp + d[remainder][1] >= p and s > 0 and tot_pt > 0:
        return (True, s-1)
    return (False, s)

t = int(raw_input())
for i in xrange(t):
    ln = raw_input().split()
    n = int(ln[0])
    s = int(ln[1])
    p = int(ln[2])
    tot_pts = map(int, ln[3:])
    res = 0
    for tot_pt in tot_pts:
        ret, s = is_ge_p(n, s, p, tot_pt)
        if ret:
            res += 1
        #print "res  " , tot_pt, res, s

    print "Case #%s: %s" % (i+1, res)
