import sys
from math import sqrt

fname = sys.argv[1].replace(".in","")
fin = open(fname+'.in', 'rU')
fout = open(fname+'.out', 'w')

T = int(fin.readline().strip())

for case in xrange(T):
    L,P,C = map(int, fin.readline().split())
    ans = 0
    while L*C < P:
        P = sqrt(L*P)
        ans += 1
    fout.write("Case #%i: %s\n" % (case+1, ans))

fin.close()
fout.close()