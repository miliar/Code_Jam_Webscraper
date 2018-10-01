import itertools
import sys


def remove_repeats(s):

    def _():
        prev = None
        for c in s:
            if c == prev:
                continue
            yield c
            prev = c

    return "".join(_())


def lcp(a, b):

    def allsame(x):
        return len(set(x)) == 1

    return "".join(
        i[0] for i in itertools.takewhile(allsame, itertools.izip(a, b)))


def alg_a(strings, aim):
    moves = 0
    for s in strings:
        while s != aim:
            moves += 1
            c = lcp(s, aim)
            a = s[len(c):]
            b = aim[len(c):]
            last = c[-1]
            if b and b[0] == last:
                s = c + last + a
            elif a and a[0] == last:
                s = c + a[1:]

    return moves


def alg_b(strings, aim):
    moves = 0
    by_length = sorted(strings, key=len)
    while len(by_length) > 1:
        a, b = by_length[:2]
        while a != b:
            c = lcp(a, b)
            last = c[-1]
            a = a[len(c):]
            b = b[len(c):]
            while a and last == a[0]:
                moves += 1
                a = a[1:]
            while b and last == b[0]:
                moves += 1
                b = b[1:]
        else:
            del by_length[0]
    return moves


def number_of_moves(strings, aim):
    return min(alg_a(strings, aim), alg_b(strings, aim))


def main():
    inputfh = sys.stdin
    outputfh = sys.stdout
    for test_number in range(1, int(inputfh.readline().strip()) + 1):
        N = int(inputfh.readline().strip())
        strings = [inputfh.readline().strip() for _ in xrange(N)]
        outputfh.write("Case #%d: " % test_number)
        without_repeats = set(map(remove_repeats, strings))
        if len(without_repeats) != 1:
            outputfh.write("Fegla won")
        else:
            aim = without_repeats.pop()
            outputfh.write(str(number_of_moves(strings, aim)))
        outputfh.write("\n")


if __name__ == "__main__":
    main()
