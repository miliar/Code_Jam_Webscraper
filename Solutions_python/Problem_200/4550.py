#!/usr/bin/env python3

t = int(input())
for i in range(1, t + 1):
    N = int(input())
    while N >= 0:
        Ns = list(map(int, str(N)))
        if (sorted(Ns) == Ns):
            print("Case #{}: {}".format(i, N))
            break
        # elif all(n in [1,0] for n in Ns):
        #     ums = ''
        #     for n in Ns:
        #         if n == 0:
        #             break
        #         else:
        #             ums += '1'
        #     N -= int(ums)
        #     
        else:
            N -= 1

