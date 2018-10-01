from math import ceil

def solve(input):
    C, F, X = map(float, input.readline().split())
    A = int(ceil((F * X - 2 * C - F * C) / (F * C)))
    t = 0
    f = 0
    for c in range(A):
        t += C / (2 + f * F)
        f += 1
    t += X / (2 + f * F)
    return "%.7f" % t

test_answer = {
    1: "1.0000000",
    2: "39.1666667",
    3: "63.9680013",
    4: "526.1904762",
}

if __name__ == '__main__':
    import sys
    test = False
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = 'test.txt'
        test = True
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    with open(file_name) as f:
        T = int(f.readline())
        for i in range(1, T + 1):
            answer = solve(f)
            if test:
                assert answer == test_answer[i]
            else:
                print "Case #%d: %s" % (i, answer)
