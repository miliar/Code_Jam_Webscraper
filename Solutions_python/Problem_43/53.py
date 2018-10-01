import sys
from multiprocessing import Pool

def func(msg):
    msg = msg.strip()
    N = list(range(37))
    N[0] = 1
    N[1] = 0
    chars = [c for c in msg]
    cset = set(chars)
    base = len(cset)
    if base < 2:
        base = 2
    #print(N,base, cset)
    t = {}
    ret = 0
    i = 0
    offset = 0
    for c in chars:
        if c not in t:
            t[c] = N[i]
            i += 1
        ret += t[c] * pow(base, len(chars) - 1 - offset)
        offset += 1
    #print(t)
    return ret

f = open(sys.argv[1])
T = int(f.readline())
tc = f.readlines()
#p = Pool(2)
rst = map(func, tc)
num = 1
for t in rst:
    print("Case #%d: %d" % (num, t))
    num += 1

    
