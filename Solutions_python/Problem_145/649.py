import os
from math import log, floor
from fractions import gcd

f_inpf = 'input.txt'
f_outf = 'output.txt'
f_in=open(f_inpf)
f_out=open(f_outf, 'w')

def next_line(f):
    line = f.readline()
    if line:
        line = line.strip()
    return line

def getclose2(n):
    res = 0
    while n >= 2.0:
        res += 1
        n/=2
    return res

def get_num(p, q):
    num = None
    x = gcd(p,q)
    p = p/x
    q= q/x
    pow_2 = log(q,2)
    if int(pow_2) != pow_2:
        return None
    x1 = getclose2(p)
#    print x1
    num = pow_2 - x1
    return int(num)

num_tc = int(next_line(f_in))
impossible = 'impossible'
resp = 'Case #%s: %s'
for i in xrange(1,num_tc+1):
    p,q = [int(_) for _ in next_line(f_in).split('/')]
    res = get_num(p, q)
    if res is None:
        res = impossible
    out = resp % (i, res)
    f_out.write('%s\n' % out)
    print out
f_in.close()
f_out.close()
