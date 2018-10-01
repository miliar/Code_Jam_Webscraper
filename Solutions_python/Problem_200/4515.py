"""
If a number is not tidy, it must be decremented until the first tidy
number is seen.

The minimum number of decrements leaves all digits to the right of the
decrease at 9.
"""


def last_tidy_number(n):
    digits = [int(d) for d in str(n)]
    i = next((i for i in range(len(digits)-1) if digits[i] > digits[i+1]), None)

    if i is None:
        return n

    for j in range(i+1, len(digits)):
        # The minimum number of decrements leaves all digits to the right of the
        # decrease at 9.
        digits[j] = 9

    digits[i] -= 1

    while i > 0 and digits[i-1] > digits[i]:
        # The minimum number of decrements leaves all digits to the right of the
        # decrease at 9.
        digits[i] = 9
        digits[i-1] -= 1
        i -= 1

    return int(''.join(map(str, digits)))


def main():
    T = int(input())

    for t in range(1, T+1):
        N = int(input())
        print('Case #{}: {}'.format(t, last_tidy_number(N)))


if __name__ == '__main__':
    main()
