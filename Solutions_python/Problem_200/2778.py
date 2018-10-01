#!/usr/bin/env python3

"""Problem B (large): Tidy Numbers"""


def last_tidy(number):
    number = number.lstrip("0")
    l_number = len(number)
    first = 0

    for i in range(l_number - 1):
        if number[i] != number[first]:
            first = i

        if number[i] > number[i + 1]:
            number = number[:first] + str(int(number[first]) - 1) \
                + "9" * (l_number - first - 1)
            break

    return int(number)


out = open("B-large.out", "w")

with open("B-large.in") as in_file:
    T = int(in_file.readline())

    assert 1 <= T <= 100

    for case in range(T):
        N = in_file.readline().strip()
        assert 1 <= int(N) <= 10 ** 18

        result = last_tidy(N)

        out.write("Case #{}: {}\n".format(case + 1, result))
