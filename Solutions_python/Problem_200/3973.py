#!/usr/bin/env python3


def look_for_error(number):
    if len(number) == 1:
        return number

    pos = 0
    old_digit = None
    same_number_count = 1
    for digit in number:
        digit = int(digit)
        if old_digit and digit < old_digit:
            return (number[:pos - same_number_count] + str(old_digit - 1) + ((len(number) - pos + same_number_count - 1) * "9")).lstrip("0")
        elif old_digit and digit == old_digit:
            same_number_count += 1
            if (pos + 1) == len(number):
                return number
        elif old_digit and digit > old_digit and (pos + 1) == len(number):
            return number
        else:
            old_digit = int(digit)
        pos += 1


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{0}: {1}".format(i, look_for_error(str(input().rstrip()))))
