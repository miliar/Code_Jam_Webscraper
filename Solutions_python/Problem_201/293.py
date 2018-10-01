import heapq

infile = open('C-large.in', 'r')
outfile = open('stalls.out', 'w')


def max_min(stalls, people):
    i = 1
    while people > 2 ** i - 1:
        i += 1
    i -= 1

    stalls -= 2 ** i - 1
    people -= 2 ** i - 1
    least = stalls // (2 ** i)
    least += people <= stalls - (2 ** i * least)
    least -= 1
    return least // 2 + (least % 2), least // 2


T = int(infile.readline())

for t in range(1, T + 1):
    N, K = map(int, infile.readline().strip().split())
    a, b = max_min(N, K)
    outfile.write("Case #{0}: {1} {2}".format(t, a, b) + '\n')
