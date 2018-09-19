#from sys import stdin as s
s = file('A-large.in', 'r')
w = file('A-large.out', 'w')
t = int(s.readline())
for j in xrange(1, t+1):
    maxs, level = s.readline().split()
    maxs = int(maxs)
    init = 0
    ans = 0
    for i, l in enumerate(level):
        if init < i:
           ans = ans + i-init
           init = i
        init = init + int(level[i])
    w.write('Case #%d: %d\n'%(j, ans))
s.close();
w.close();
