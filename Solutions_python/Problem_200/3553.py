def is_tidy(number):
    return int(''.join(sorted(str(number)))) == number


def previous_tidy(number):
    p = None
    tidy = [int(n) for n in str(number)]
    for i, x in enumerate(tidy[::-1]):
        if p is None:
            p = x
            continue

        if x > p:
            tidy[-i:] = [9] * i
            tidy[-i - 1] = x - 1

        p = tidy[-i - 1]

    return int(''.join(map(str, tidy)))


def main():
    n = int(raw_input())
    for i in xrange(n):
        print "Case #{}: {}".format(i + 1, previous_tidy(int(raw_input())))


if __name__ == "__main__":
    main()
