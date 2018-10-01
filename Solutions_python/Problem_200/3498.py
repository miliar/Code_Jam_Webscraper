#!/usr/bin/env python
def solve():
    s = str(N)

    while True:
        if len(s) == 1:
            return int(s)
        i = 0
        while i < len(s) - 1:
            if int(s[i]) > int(s[i + 1]):
                s = str(int(s[:i+1] + "0" * (len(s) - i - 1)) - 1)
                break
            i += 1
            if i == len(s) -1:
                return int(s)

T = input()
for i in range(1, T + 1):
    N = input()
    last_tidy = solve()
    print "Case #%d: %d" % (i, last_tidy)
