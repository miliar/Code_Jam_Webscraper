import sys

memo = {}

def main(fin, fout):

    T = int(fin.readline())
    for t in range(1,T+1):
        N, X, Y = tuple(abs(int(x)) for x in fin.readline().split())

        if t == 58:
            pass
        print("Case #{:d}: {:.6f}".format(t, solve(N,X,Y)))

def factorial(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    res =  n * factorial(n-1)
    memo[n] = res
    return memo[n]

def permutations(tot, part):
    if part == 0:
        return 1
    if tot == part:
        return 1
    return factorial(tot) / (factorial(part) * factorial(tot-part))

def solve(N,X,Y):
    layer = ((X+Y) / 2) +1
    layerp = layer-1

    full = layer * (2*layer - 1)
    fullp = layerp * (2*layerp -1)

    if N > full:
        return 1.0
    if N <= fullp:
        return 0.0

    if X == 0:
        if N == full:
            return 1.0
        else:
            return 0.0

    items_left = N-fullp
    max_at_other_side = 2*(layer-1)
    if items_left >= max_at_other_side + Y + 1:
        return 1.0

    # calculate the chances that not Y+1 out of items_left times the correct side is chosen
    # if items_left <= max_at_other_side:

    if Y + 1 > items_left:
        return 0.0

    perms = 0
    for i in range(0,Y+1):
        perms += permutations(items_left, i)

    return 1 - (0.5 ** items_left) * perms

    # else:
    #     s = 0
    #     #changes that the other side fills up
    #     for i in range(max_at_other_side, items_left):
    #         s += (0.5 ** (i-1)) * permutations(i-1, max_at_other_side-1)
    #
    #     #changes when the other side isn't filled up
    #     items_needed = Y+1
    #     for i in range(items_left-max_at_other_side+1, items_needed):
    #         s += (0.5 ** items_left) * permutations(items_left, i)
    #     return 1 - s


    # return 0.1234

    # return 1 - s


if __name__=="__main__":
    if len(sys.argv) > 1:
        fin = open(sys.argv[1])
    else:
        fin = sys.stdin

    if len(sys.argv) > 2:
        fout = open(sys.argv[2], 'w')
    else:
        fout = sys.stdout

    main(fin,fout)
