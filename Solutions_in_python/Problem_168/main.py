DIRS = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}

def run(data):
    coords = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item != '.':
                coords.append((x, y))
    changes = 0
    for x, y in coords:
        result = dict([(i, False) for i in "^v<>"])
        for d, (dx, dy) in DIRS.items():
            nx, ny = x, y
            while 0 <= nx + dx < len(data[0]) and 0 <= ny + dy < len(data):
                nx += dx
                ny += dy
                if data[ny][nx] != '.':
                    result[d] = True
        if not result[data[y][x]]:
            if any(result.values()):
                changes += 1
            else:
                return "IMPOSSIBLE"
    return changes

f = open("large.in", "rU")
text = f.readlines()[1:]
f.close()
cases = []

i = 0
while i < len(text):
    r, c = map(int, text[i].split())
    cases.append([])
    for j in range(r):
        cases[-1].append(text[i + j + 1].strip())
    i += r + 1

for i, data in enumerate(cases):
    print("Case #{}: {}".format(i+1, run(data)))
