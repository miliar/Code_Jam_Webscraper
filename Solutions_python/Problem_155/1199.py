def solve_one ( data ):
    smax  = int(data[0])
    sdata = map(int, list(data[1]))

    nfriends = 0
    for i in xrange(1, len(sdata)):
        if i > sdata[i-1]:
            # we need more people
            nfriends += i - sdata[i-1]
            sdata[i]  = sdata[i] + i
        else:
            sdata[i]  = sdata[i] + sdata[i-1]
    return nfriends


def solve( in_stream ):
    n = int(in_stream.readline())

    test_cases = [
        in_stream.readline().split()
        for t in xrange(n)
    ]
    s = 'Case #{0}: {1}\n'

    results = [
        s.format(i+1, solve_one(t))
        for i, t in enumerate(test_cases)
    ]

    return results


if __name__ == '__main__':
    import sys

    # read input
    in_resource = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin
    with in_resource as in_stream:
        result = solve( in_stream )

    # write output
    out_resource = open(sys.argv[2], 'w') if len(sys.argv) > 2 else sys.stdout
    with out_resource as out_stream:
        out_resource.writelines(result)

