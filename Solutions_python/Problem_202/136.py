updates = []
score = 0
t= int(input())  # read a line with a single integer

def upgrade(i, j, g):
    orthogonal = True
    for ni in range(len(g)):
        if ni == i:
            continue
        if g[ni][j] in ['o', 'x']:
            orthogonal = False

    for nj in range(len(g)):
        if nj == j:
            continue
        if g[i][nj] in ['o', 'x']:
            orthogonal = False

    diagonal = True
    for d in range(-1 * (len(g) - 1), len(g)):
        if d == 0:
            continue
        if i + d >= 0 and i + d < len(g) and j + d >= 0 and j + d < len(g):
            if g[i + d][j + d] in ['o', '+']:
                diagonal = False

        if i - d >= 0 and i - d < len(g) and j + d >= 0 and j + d < len(g):
            if g[i - d][j + d] in ['o', '+']:
                diagonal = False

    if orthogonal and diagonal:
        if g[i][j] != 'o':
            g[i][j] = 'o'
            updates.append(('o', i + 1, j + 1))
    elif orthogonal:
        if g[i][j] != 'x':
            g[i][j] = 'x'
            updates.append(('x', i + 1, j + 1))
    elif diagonal:
        if g[i][j] != '+':
            g[i][j] = '+'
            updates.append(('+', i + 1, j + 1))

for k in range(1, t + 1):

    updates = []
    score = 0

    n, m = [int(x) for x in raw_input().split(" ")]

    g = [['.' for i in range(n)] for j in range(n)]
  
    for i in range(m):
        s, r, c = raw_input().split(" ")
        g[int(r) - 1][int(c) - 1] = s

    order = range(n - 1)
    order.insert(0, n - 1)
    for i in order:
        for j in range(n):
            upgrade(i, j, g)
            if g[i][j] in ['x', '+']:
                score += 1
            elif g[i][j] == 'o':
                score += 2

    print("Case #{}: {} {}".format(k, score, len(updates)))

    for u in updates:
        print(" ".join([str(x) for x in u]))
