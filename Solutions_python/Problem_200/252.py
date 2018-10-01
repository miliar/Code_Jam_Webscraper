def num_to_digits(num):
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num //= 10
    return digits


def digits_to_num(digits):
    num = 0
    for digit, i in zip(digits, range(len(digits) - 1, -1, -1)):
        num += 10 ** i * digit
    return num


def is_tidy(digits):
    for prev, curr in zip(digits[:-1], digits[1:]):
        if curr < prev:
            return False
    return True


def find_problematic_i(digits):
    for i, (prev, curr) in zip(range(len(digits)),
                               zip(digits[:-1], digits[1:])):
        if curr < prev:
            return i + 1

num_tests = int(input())
for test in range(1, num_tests + 1):
    num = int(input())
    digits = num_to_digits(num)
    while not is_tidy(digits):
        problematic_i = find_problematic_i(digits)
        # print('num: {}'.format(digits_to_num(digits)))
        # print('problematic_i: {}'.format(problematic_i))
        digits[problematic_i - 1] -= 1
        digits[problematic_i:] = [9] * (len(digits) - problematic_i)
        # if digits[problematic_i] == 0:
        #     digits = [9] * (len(digits) - 1)
        # else:
        #     if problematic_i - 2 >= 0 and digits[problematic_i - 1]:
        #         digits[problematic_i - 1] =
        #     digits[problematic_i - 1] = digits[problematic_i]
        #     for i in range(problematic_i, len(digits)):
        #         digits[i] = 9

    print('Case #{}: {}'.format(test, digits_to_num(digits)))
