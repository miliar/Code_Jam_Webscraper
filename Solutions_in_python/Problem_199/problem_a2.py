import sys

def next_line(f):
    line = f.readline()
    if line[-1] == '\n':
        line = line[:-1]
    return line.split(' ')


with open(len(sys.argv) > 1 and sys.argv[1] or 'input/A-small-attempt0.in', 'r') as f:
    n_cases = int(next_line(f)[0])
    for case in range(1, n_cases+1):
        row, K_str = next_line(f)
        K = int(K_str)
        N = len(row)
        correct = map(lambda x: x=='+', row)
        movements = 0
        for i in range(N):
            if correct[i]:
                continue
            if i+K <= N and not correct[i]:
                for j in range(i, i+K):
                    correct[j] = not correct[j]
                movements += 1

        if all(correct):
            print("Case #%d: %d" % (case, movements))
        else:
            print("Case #%d: IMPOSSIBLE" % case)
