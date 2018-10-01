import sys

def solve(cakes, size):
    changes = 0

    for i in range(0, len(cakes) - size + 1):
        if cakes[i] == '-':
            changes += 1
            for j in range(0, size):
                cakes[i + j] = '+' if cakes[i + j] == '-' else '-'

    print(cakes)

    for i in range(0, len(cakes)):
        if cakes[i] == '-':
            return "IMPOSSIBLE"

    return changes


testname = sys.argv[1]

print(testname)

fin = open(testname + '.in', 'r')
fout = open(testname + '.out', 'w')

ntest = int(fin.readline().strip())

for t in range(1, ntest + 1):
    line = fin.readline().strip().split()
    ans = solve(list(line[0]), int(line[1]))
    fout.write("Case #{}: {}\n".format(t,ans))