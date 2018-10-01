#!/usr/bin/python
import sys

def solve(first, second):
    card = None
    for c in first:
        if c in second:
            if card is not None:
                return ("Bad magician!",)
            else:
                card = c
    if card is None:
        return ("Volunteer cheated!",)

    return (card,)

def parse_case(*args):
    answer_A = R(int)
    cards_A = [map(int, R().split()) for _ in range(4)]
    answer_B = R(int)
    cards_B = [map(int, R().split()) for _ in range(4)]
    return (cards_A[answer_A - 1], cards_B[answer_B - 1])

def format_ret(ret):
    return str(ret)

def R(cast = None):
    ret = sys.stdin.readline().strip()
    if cast is not None:
        ret = cast(ret)
    return ret

def W(msg, *args):
    sys.stdout.write((msg + "\n") % args)

def main():
    cases = R(int)
    for i in range(1,cases+1):
        ret = solve(*parse_case())
        W("Case #%d: %s", i, format_ret(*ret))

if __name__ == '__main__':
    main()
