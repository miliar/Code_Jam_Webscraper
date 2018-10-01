import sys
import math


def r1(instream, type=int):
    return type(instream.readline().strip())


def ra(instream, type=int):
    return [type(x) for x in instream.readline().strip().split(" ")]


def solve(instream):
    answer1 = r1(instream)
    cards1 = [ra(instream) for _ in range(4)]
    answer2 = r1(instream)
    cards2 = [ra(instream) for _ in range(4)]

    row1 = cards1[answer1 - 1]
    row2 = cards2[answer2 - 1]

    common = [x for x in row1 if x in row2]
    if not common:
        return "Volunteer cheated!"

    if len(common) > 1:
        return "Bad magician!"

    return common[0]


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
