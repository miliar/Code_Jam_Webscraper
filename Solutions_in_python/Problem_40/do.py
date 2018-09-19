import sys
from tree import *
fdin = open(sys.argv[1],'r')
fdout = open(sys.argv[2],'w')

n = int(fdin.readline())
for i in range(n):
    ln = int(fdin.readline())
    tmp_lines = []
    for j in range(ln):
        tmp_lines.append(fdin.readline())
    root = parse(build_line(tmp_lines))
    cn = int(fdin.readline())
    fdout.write('Case #%d:\n' % (i+1))
    for j in range(cn):
        af = fdin.readline()
        af = af.split()
        af = af[2:]
        p = cute_rate(root, af)
        fdout.write('%.7f\n' % p)

fdin.close()
fdout.close()
