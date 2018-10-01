result = {}


def fill(baths, where):
    r = 0
    result = right[:]
    for i in where:
        if right[i] == -1:
            r = 0
        else:
            result[i] = r
            r += 1
    return result


with open('C-small-1-attempt0.in') as infile:
    t = int(infile.readline())

    for i in xrange(1, t + 1):
        n, k = [int(s) for s in infile.readline().split(' ')]
        right = [-1] + [0] * n + [-1]
        left = [-1] + [0] * n + [-1]

        for j in xrange(k):
            right = fill(right, reversed(xrange(n + 2)))
            left = fill(left, xrange(n + 2))

            # print right
            # print left

            bath = 0

            for y in xrange(n + 2):
                if right[y] == -1:
                    next
                else:
                    if min(right[y], left[y]) == min(right[bath], left[bath]):
                        if max(right[y], left[y]) > max(right[bath], left[bath]):
                            bath = y
                    elif min(right[y], left[y]) > min(right[bath], left[bath]):
                        bath = y

                # print bath

            R = min(right[bath], left[bath])
            L = max(right[bath], left[bath])

            right[bath] = -1
            left[bath] = -1

        result[i] = (L, R)

with open('C-small-1-attempt0.out', 'w') as outFile:
    for i in result:
        outFile.write("Case #{}: {} {}\n".format(i, result[i][0], result[i][1]))
