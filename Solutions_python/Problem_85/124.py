import sys

def readline():
    return sys.stdin.readline().strip()

def solve(values):
    L = values[0]
    t = values[1]
    N = values[2]
    C = values[3]
    a = values[4:]

    d = 0.5 * t

    cum = [0]
    points = []
    s = 0
    j = 0
    for i in range(N):
        points.append([i, a[j % len(a)]])
        s += a[j % len(a)]
        cum.append(s)
        j += 1

    # See where we will be
    for idx, val in enumerate(cum):
        if val >= d:
            break

    if val == d:
        best = points[idx:]
    else:
        best = [[idx - 1, (val - d)]] + points[idx:]

    best.sort(cmp = lambda x, y: cmp(y[1], x[1]))
    # Pick the N top ones
    idxes = []
    for i in range(L):
        best[i][0] = True
    for flag, dist in best:
        if flag is True:
            t += dist
        else:
            t += 2 * dist
    return t

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        print "Case #%d: %d" % (i + 1, solve([int(n) for n in readline().split()]))

if __name__ == "__main__":
    main()
