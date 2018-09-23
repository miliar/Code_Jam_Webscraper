import fileinput

def doflip(seq, i, k):
    for j in range(i, min(i + k, len(seq))):
        seq[j] = '-' if seq[j] == '+' else '+'
    return seq[:]


def solve(seq, k):
    seq = list(seq)
    i = 0
    flips = 0
    while i < len(seq):
        if seq[i] == "-":
            if i + k > len(seq):
                return -1
            seq = doflip(seq, i, k)
            flips += 1
        i += 1
    return flips

f = fileinput.input()
T = int(f.readline())
for case in range(1, T + 1):
    seq, k = [x for x in f.readline().split()]
    answer = solve(seq, int(k))
    print("Case #{0}: {1}".format(case, answer if answer != -1 else "IMPOSSIBLE"))
