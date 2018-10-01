#!/usr/bin/env python

#TEST = """4
#4 11111
#1 09
#5 110011
#0 1"""
#input = iter(TEST.splitlines()).__next__

T = int(input())
for case in range(1, T+1):
    smax, audience = input().split()
    smax = int(smax)
    assert( len(audience) == smax+1 )
    standing = 0
    plants = 0
    for shyness, count in enumerate(audience):
        count = int(count)
        if shyness <= standing:
            standing += count
        elif count:
            gap = shyness - standing
            plants += gap
            standing += (gap + count)

    print("Case #%s: %s" % (case, plants))

