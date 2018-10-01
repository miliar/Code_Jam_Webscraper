
def flipPancake(pancake):
    if pancake == '+':
        pancake = '-'
    else:
        pancake = '+'

    return pancake

def flipRight(row, index, n):
    for i in range(index, index+n):
        row[i] = flipPancake(row[i])

    return row


def solvePancake(row, k):
    flips = 0

    for i in range(0, len(row)-k+1):
        if row[i] == '-':
            row = flipRight(row, i, k)
            flips += 1

    return "IMPOSSIBLE" if '-' in row else flips

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    p, k = input().split(" ")
    k = int(k)

    print("Case #{}: {} ".format(i, solvePancake(list(p), k)))

