import math
f = open('C-small-attempt1.in')
fo = open('C-out.txt', 'w')
for z in range(int(f.readline().strip())):
    lo, hi = [int(x) for x in f.readline().strip().split()]
    c = math.ceil(math.sqrt(lo))
    end = math.floor(math.sqrt(hi))
    a = 0
    while c <= end:
        v = c**2
        if str(c) == str(c)[::-1] and str(v) == (str(v)[::-1]): a += 1
        c += 1
    fo.write('Case #%d: %d\n' %((z+1), a))
f.close(), fo.close()
