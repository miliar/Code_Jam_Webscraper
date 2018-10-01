def is_tidy(num):
    snum = str(num)
    iprev = 0
    for c in snum:
        i = int(c)
        if i < iprev:
            return False
        iprev = i
    return True

def build_idx(upperbound):
    last_tidy = 0
    ltidx = [0]
    for i in range(1, upperbound+1):
        it = is_tidy(i)
        if it:
            last_tidy = i
        ltidx.append(last_tidy)
    return ltidx

def get_last_tidy(N):
    sN = str(N)
    l = len(sN)
    dprev = 0
    last_inc_idx = 0
    for i in range(0, l):
        c = sN[i]
        d = int(c)
        if d < dprev:
            # its not tidy!
            # now we build the last tidy string
            # start with the tidy part, up to the last increase
            lts = sN[0:last_inc_idx]
            # get the next digit and reduce by 1
            nd = str(int(sN[last_inc_idx])-1)
            lts = lts + nd
            # then fill the remainder with 9s
            while len(lts) < l:
                lts = lts + "9"
            return int(lts)
        if d > dprev:
            last_inc_idx = i
        dprev = d
    # it's tidy!
    return N

"""
inputs = [132, 1000, 7]
# , 111111111111111110

ltidx = build_idx(100000)
for input1 in inputs:
    print "%s %s %s" % (input1, ltidx[input1], get_last_tidy(input1))

for input1 in range(1, 100000):
    i1 = ltidx[input1]
    i2 = get_last_tidy(input1)
    if not i1 == i2:
        print "%s %s %s" % (input1, i1, i2)
"""

lines = open("B-large (1).in").readlines()

T = int(lines[0])
caseno = 1
for line in lines[1:T+1]:
    line = line.lstrip().rstrip()
    ans = get_last_tidy(int(line))
    print 'Case #%s: %s' % (caseno, ans)
    caseno = caseno + 1
