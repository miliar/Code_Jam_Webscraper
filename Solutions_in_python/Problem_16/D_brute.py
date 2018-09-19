from util import *

def perms(ns):
    if not ns:
        return [[]]
    else:
        return [[n] + p for (i,n) in enumerate(ns) for p in perms(ns[:i] + ns[i+1:])]



def solve(n):
    k = input()
    S = raw_input()

    ps = perms(range(k))

    def cost(p):
        def get(i):
            q,r = divmod(i,k)
            i_ = q*k + p[r]
            return S[i_]

        if not S:
            return 0
        else:
            c = 1
            i = 1
            while i < len(S):
                if get(i) != get(i-1):
                    c += 1
                i+=1
            return c

    return min(cost(p) for p in ps)

drive(solve)
