#!/usr/bin/python
# -*- coding:Utf-8 -*-

n = int(input())
output = list()

for i in range(n) :
    case = input()
    tab = [int(c) for c in case.split()[1]]
    total = 0
    out = 0
    for d in range(int(case.split()[0])+1) :
        if d > total :
            total += 1
            out += 1
        total += tab[d]
    output.append("Case #%d: %d" % (i+1, out))
print("\n".join(output))
