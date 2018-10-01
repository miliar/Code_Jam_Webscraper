# lizesheng
#


def solve(n, k):
    n, k = int(n), int(k)

    d = {n: 1}
    while k:
        block = max(d.keys())
        ls = (block-1)//2
        rs = block-1-ls
        ff = d[block]  # fastforward
        if ff >= k:
            return max(ls, rs), min(ls, rs)

        k -= ff
        del d[block]
        d[ls] = d.get(ls, 0) + ff
        d[rs] = d.get(rs, 0) + ff

    assert False, "Shouldn't have reached here."
    return


t = int(input())
for icase in range(1, t + 1):
    a, b = input().split(" ")
    print("Case #{}: {} {}".format(icase, *solve(a, b)))
