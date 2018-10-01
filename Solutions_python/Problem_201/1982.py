#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    N, K = [int(x) for x in input().split()]

    spaces = {(N,0)}


    out = []
    inbox = {N: 1}


    def add_to_inbox(x, qty):
        if x > 0:
            if x in inbox:
                inbox[x] += qty
            else:
                inbox[x] = qty



    while len(out) < K: # odbrze?
        m = max(inbox)
        qty = inbox[m]
        out = out + [m] * qty
        del inbox[m]
        add_to_inbox(m // 2, qty)
        add_to_inbox((m-1) // 2, qty)


    m = out[K - 1]
    print("Case #{}: {} {}".format(t, m // 2, max(0, (m-1) // 2)))
