# -*- coding: utf-8 -*-
__author__ = 'Lauri Elias'

with open('input.txt') as f:
    content = f.readlines()

out = open('output.txt', 'w')
cases = int(content[0].strip())
for i in range(cases):
    diners = int(content[i * 2 + 1].strip())
    cakes = list(map(int, content[i * 2 + 2].strip().split()))
    min_minutes = max(cakes)
    Z = 2
    while Z < min_minutes:
        min_minutes = min(min_minutes, sum([(amount - 1) // Z for amount in cakes]) + Z)
        Z += 1
    out.write('Case #%d: %s\n' % ((i + 1), min_minutes))
out.close()