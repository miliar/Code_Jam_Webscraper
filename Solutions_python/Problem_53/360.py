#!/usr/bin/python

pot2 = []
for i in range(31):
    pot2.append((2**i)-1)

for i in range(input()):
    N, K = map(int, raw_input().split())
    if ((K & pot2[N]) == pot2[N]):
        print 'Case #%s: ON' % (i + 1)
    else:
        print 'Case #%s: OFF' % (i + 1)
