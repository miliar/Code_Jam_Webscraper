import sys
r = sys.stdin.readline

T = int(r())

delta = 1e-6

def naomi_pts_normal(ns, ks):
    accum = 0
    while ns:
        n = ns.pop()
        possible_ks = [x for x in ks if x > n]
        if possible_ks:
            k = min(possible_ks)
        else:
            k = min(ks)
        ks.remove(k)
        if n > k:
            accum += 1
    return accum
        
def naomi_pts_optimal(ns, ks):
    accum = 0
    while ns:
        k_worst = min(ks)
        n_best = max(ns)
        defo_losers = len([n for n in ns if n < k_worst])
        defo_k_winners = len([k for k in ks if k > n_best])
        for i in range(0, max(defo_losers, defo_k_winners)):
            ns.remove(min(ns))
            ks.remove(max(ks))
        if not ns:
            break
        ns.remove(min(ns))
        ks.remove(min(ks))
        accum += 1

    return accum

for t in range(T):
    N = int(r())
    naomis = sorted(map(float, r().split()))
    kens = sorted(map(float, r().split()))
    
    normal_game = naomi_pts_normal([x for x in naomis], [k for k in kens])
    cheat = naomi_pts_optimal(naomis, kens)
    print("Case #%d: %d %d" % (t+1, cheat, normal_game))
