def flip(cake, idx, k):
    return cake[:idx] + ''.join([('+' if x == '-' else '-') for x in cake[idx:idx + k]]) + cake[idx + k:]

def solve(pancake, k):
    backup = str(pancake)
    count = 0
    l = len(pancake)
    for i in range(l - k + 1):
        if pancake[i] == '-':
            pancake = flip(pancake, i, k)
            count += 1
    if '-' in pancake:
        return None

    return count

for t in range(1, int(raw_input()) + 1):
    p, k = raw_input().strip().split()
    k = int(k)
    sol = solve(p, k)
    if sol is None:
        print("Case #%d: IMPOSSIBLE" % (t))
    else:
        print("Case #%d: %s" % (t, sol))