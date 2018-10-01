def solve_first_method(mis):
    result = 0
    for x in xrange(1, len(mis)):
        prev = mis[x-1]
        nex  = mis[x]
        result += max(0, prev - nex)
    return result

def solve_second_method(mis):
    # try to determine the minimum speed required
    rate = 0
    for x in xrange(1, len(mis)):
        prev = mis[x-1]
        nex  = mis[x]
        rate = max(rate, prev - nex)

    result = 0
    for mi in mis[:-1]:
        result += min(mi, rate)

    return result


def solve_one_slow(mis):
    return mis

def solve_one(mis):
    return '{0} {1}'.format(
            solve_first_method(mis),
            solve_second_method(mis),
        )

def main(instream, outstream, slow):
    n = int( instream.readline() )

    for i in xrange(n):
        instream.readline()
        mis = map(int, instream.readline().split())
        result = solve_one_slow(mis) if slow else solve_one(mis)
        outstream.writelines('Case #{0}: {1}\n'.format(i+1, result))


if __name__ == '__main__':
    import sys

    instream  = open(sys.argv[1], 'r') if len( sys.argv ) > 1 else sys.stdin
    outstream = open(sys.argv[2], 'w') if len( sys.argv ) > 2 else sys.stdout
    slow      = len( sys.argv ) > 3

    with instream, outstream:
        main(instream, outstream, slow)