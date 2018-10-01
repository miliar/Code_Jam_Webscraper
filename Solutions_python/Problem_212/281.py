from collections import Counter


def solve(p, groups):
    mod_groups = Counter()
    for group in groups:
        mod_groups[group % p] += 1

    pack_sum = 0
    whole_pack_groups = 0
    while sum(mod_groups.values()):
        # If starting with a fresh pack, add one to the balanced group count
        if pack_sum == 0:
            whole_pack_groups += 1

        # Take a group that balances first, or if not possible, the smallest group
        ideal_pack = (p - pack_sum) % p
        if mod_groups[ideal_pack] > 0:
            pack_sum += ideal_pack
            mod_groups[ideal_pack] -= 1
            if mod_groups[ideal_pack] == 0:
                del mod_groups[ideal_pack]
        else:
            pack_sum += min(mod_groups)
            mod_groups[min(mod_groups)] -= 1
            if mod_groups[min(mod_groups)] == 0:
                del mod_groups[min(mod_groups)]
        pack_sum %= p
    return whole_pack_groups


input()
case = 0
while True:
    case += 1
    try:
        n, p = map(int, input().split(' '))
        groups = map(int, input().split(' '))
    except:
        break
    print('Case #{}: {}'.format(case, solve(p, groups)))

