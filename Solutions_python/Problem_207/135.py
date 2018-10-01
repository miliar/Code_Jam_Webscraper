import sys
from solve import solve

def solve_secondary(n, colors):
    index = 0
    retval = {}
    for secondary, match in (('O', 'B'), ('G', 'R'), ('V', 'Y')):
        stable = []
        for _ in range(colors[secondary]):
            if colors[match] == 0:
                return 'IMPOSSIBLE'
            if _ == 0:
                if colors[match] == 1:
                    return 'IMPOSSIBLE'
                colors[match] -= 2
                stable.append(match)
                stable.append(secondary)
                stable.append(match)
            else:
                colors[match] -= 1
                stable.append(secondary)
                stable.append(match)
                index += 2
        colors[secondary] = 0
        retval[match] = ''.join(stable)
    return retval

t = int(next(sys.stdin))
for test in range(t):
    arr = [int(s) for s in next(sys.stdin).strip().split(' ')]
    n = arr[0]
    colors = {
        'R': arr[1],
        'O': arr[2],
        'Y': arr[3],
        'G': arr[4],
        'B': arr[5],
        'V': arr[6]
    }
    unique_colors = [v for v in colors.values() if v > 0]
    if len(unique_colors) <= 2:
        print('Case #{}: {}'.format(test+1, solve(n, colors)))
        continue
    secondaries = solve_secondary(n, colors)
    if secondaries != 'IMPOSSIBLE':
        should_skip = False
        for primary in ('B', 'R', 'Y'):
            if secondaries[primary]:
                colors[primary] += 1
        sol = solve(sum(colors.values()), colors)
        if sol != 'IMPOSSIBLE':
            for primary in ('B', 'R', 'Y'):
                if secondaries[primary]:
                    assert primary in sol
                    index = sol.index(primary)
                    sol = sol[:index] + secondaries[primary] + sol[index+1:]
            assert len(sol) == n
    else:
        sol = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(test+1, sol))
