def xor (a, b):
    return a ^ b
def Sum (a, b):
    return a + b

inFile = open('input.txt', 'r')
outFile = open('output.txt', 'w')

piles = [[],[]]

T = int( inFile.readline() )

for j in range(1, T + 1):
    result = -1

    N = int( inFile.readline() )

    bag = [int (x) for x in inFile.readline().split(' ')]

    for step in xrange(1, pow(2, N) - 1):
        piles[0] = [0]
        piles[1] = [0]
        i = 0
        while step != 0:
            pile = step % 2
            step /= 2
            piles[pile].append(bag[i])
            i += 1
        for i in range(i, N):
            piles[0].append(bag[i])

        pile0 = reduce(xor, piles[0])
        pile1 = reduce(xor, piles[1])

        realSum0 = reduce(Sum, piles[0])
        realSum1 = reduce(Sum, piles[1])

        if pile0 == pile1 and result < max(realSum0, realSum1):
            result = max(realSum0, realSum1)

    if result != -1:
        outFile.write("Case #%d: %d\n" % (j, result))
    else:
        outFile.write("Case #%d: NO\n" % j)

inFile.close()
outFile.close()
