import sys
import re

lines = sys.stdin.readlines()

p = re.compile('(\d+) (\d+) (\d+)')
m = p.match(lines.pop(0))

L = int(m.group(1))
D = int(m.group(2))
N = int(m.group(3))

#~ print L, D, N

ins = []
for l in range(0, D):
    ins.append(lines.pop(0).strip())

res = []
for l in range(0, N):
    res.append(lines.pop(0).replace('(','[').replace(')',']').strip())

#~ print 'in', ins
#~ print 're', res

for case in range(0, N):
    count = 0
    r = res[case]
    p = re.compile(r)
    for i in ins:
        if p.match(i) is not None:
            count += 1
    print 'Case #%d: %d' % (case + 1, count)
