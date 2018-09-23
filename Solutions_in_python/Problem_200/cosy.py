import sys


def is_cosy(x):
    # type: (int) -> bool
    y = str(x)
    prev_digit = y[0]
    for digit in y:
        if int(digit) < int(prev_digit):
            return False
        prev_digit = digit
    return True


def brute_force(n):
    # type: (int) -> str
    while not is_cosy(n):
        print "%d\r" % n,
        n -= 1
    res = '%d' % n
    return res


def flatten(n):
    pass


def optimised(n):
    # type: (int) -> str
    digits = str(n)
    prev_digit = digits[0]
    if is_cosy(n):
        return '%d' % n
    for idx, digit in enumerate(digits):
        # import pdb; pdb.set_trace()
        if int(digit) < int(prev_digit):
            prov = str(int(prev_digit) - 1)
            temp = digits[0:idx-1] + prov + ('9' * (len(digits) - idx))
            print temp
            if not is_cosy(int(temp)):
                return optimised(int(temp))
            return '%d' % int(temp)
        prev_digit = digit
    return 'wot'


def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()

    t = int(lines.pop(0))
    assert t == len(lines)

    results = []
    for idx, case in enumerate(lines, 1):
        n = int(case.strip())
        print n
        if n <= 1000:
            brute = brute_force(n)
            opt = optimised(n)
            assert opt == brute, "%s != %s" % (opt, brute)
        else:
            opt = optimised(n)
        case_str = "Case #%d: %s" % (idx, opt)
        print case_str
        results.append(case_str + '\n')

    with open(sys.argv[1] + ".out", "w") as fp:
        fp.writelines(results)


if __name__ == "__main__":
    main()
