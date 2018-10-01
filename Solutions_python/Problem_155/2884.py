"""
Standing Ovation
"""

from __future__ import print_function

RESULT_FORMAT = "Case #{case}: {result}"


def random_case(level=1000):

    from random import randint

    level = randint(0, level)
    counts = [randint(0, 9) for _ in range(level)]

    return level, counts


def read_case():
    """
    Reads data for case.
    Returns (level, counts)
    """

    level, counts = input().split()

    level = int(level)

    counts = (int(count) for count in counts)

    return level, counts


def process_case(level, counts):

    extra = 0
    total = 0

    for level, count in enumerate(counts):
        if count and (total + extra) < level:
            extra += level - (total + extra)
        total += count

    return extra


def support_2():
    """
    http://stackoverflow.com/questions/954834/how-do-i-use-raw-input-in-python-3-1
    """

    try:
        global input
        import __builtin__
        input = getattr(__builtin__, 'raw_input')
    except (ImportError, AttributeError):
        pass


def main():

    import sys
    sys.stdin = open('1.testcase', 'r')

    support_2()

    cases = int(input())

    for i in range(cases):
        result = process_case(*read_case())
        print(RESULT_FORMAT.format(result=result,
                                   case=(i+1)))


if __name__ == "__main__":
    main()
