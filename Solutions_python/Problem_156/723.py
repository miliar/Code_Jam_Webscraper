memo = {}
import sys
sys.setrecursionlimit(1000)

def time(ps):

    ps = tuple(reversed(sorted(ps)))

    if ps in memo:
        return memo[ps]
    if ps[0] == 1:
        return 1

    # split the biggest stacks
    result = ps[0]

    for k in range(1, ps[0] - 1):
        if k > (ps[0] - k):
            break

        special_ps = []
        special = 0
        for i, p in enumerate(ps):
            if p != ps[0]:
                special_ps.extend(ps[i:])
                break
            special_ps.extend((ps[0] - k, k))
            special += 1

        result = min(special + time(special_ps), result)

    memo[ps] = result
    return result


def test():

    assert time((3,)) == 3
    assert time((1, 2, 1, 2)) == 2
    assert time((4,)) == 3
    from random import randint
    #N = 1000
    #data = [randint(1, N) for _ in range(N)]
    #print time(data)


if __name__ == '__main__':

    import sys

    test()

    data = open(sys.argv[1] + '.in').readlines()
    T = int(data[0].strip())

    with open(sys.argv[1] + '.out', 'w') as outfile:
        for i in range(T):
            D = int(data[2 * i + 1].strip())
            ps = map(int, data[2 * i + 2].strip().split())
            outfile.write("Case #%i: %i\n" % (i + 1, time(ps)))
