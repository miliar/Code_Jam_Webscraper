# ertug (Ertug Karamatli)

import sys
import re

f = file(sys.argv[1])

ln = 0

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

case = 1
for line in f:
    line = line.strip()
    if line == '': continue
    if ln != 0:
        N = int(line)
        perms = []
        for p in all_perms(str(N)):
            perms.append(int(p))
        for p in all_perms(str(N)+'0'):
            perms.append(int(p))
        for p in all_perms(str(N)+'00'):
            perms.append(int(p))
        perms = list(set(perms))
        perms.sort()
        #print N, perms
        if perms.index(N) + 1 == len(perms):
            pe = perms[0]
        else:
            pe = perms[perms.index(N)+1]
        print 'Case #%s: %s' % (case, pe)
        case += 1
        sys.stdout.flush()

    ln += 1

