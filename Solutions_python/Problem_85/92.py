import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
  T = int(f.readline().strip())
  for t in range(T):
    print "Case #%s:" % (t+1),
    nums = [int(x) for x in f.readline().strip().split()]
    L, t, N, C = nums[:4]
    a = nums[4:]
    assert C == len(a)
    distances = (a * (N/C + 1))[:N]
    time = sum(distances) * 2
    total = 0
    dxs = iter(distances)
    try:
        while total*2 < t:
            dx = dxs.next()
            total += dx
    except StopIteration:
        print time
        continue
    crossoverSaving = total - t/2
    counts = defaultdict(int)
    for dx in dxs:
        counts[dx] += 1
    for dx, n in reversed(sorted(counts.items())):
        if L > n:
            time -= dx * n
            L -= n
        else:
            time -= dx * L
            if crossoverSaving > dx:
                time = time + dx - crossoverSaving
            break
    print time
