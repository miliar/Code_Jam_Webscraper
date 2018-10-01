#!/usr/bin/env python

glang = ' abcdefghijklmonpqrstuvwxyz'
eng = ' yhesocvxduiglkbrztnwjpfmaq'

fh = file('input.txt', 'r')
t = fh.readline()
t = t.replace('\n', '')
t = int(t)
out = file('out.txt', 'w')

for case in range(0, t):
    str = fh.readline()
    str = str.replace('\n', '')
    res = ''
    for c in str:
        i = glang.index(c)
        res = res+eng[i]
    print 'Case #%d: %s' % (case+1, res)
    out.write('Case #%d: %s\n' % (case+1, res))
    

out.close()
fh.close()


