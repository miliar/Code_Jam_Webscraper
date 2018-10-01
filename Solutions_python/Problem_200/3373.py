#/bin/env python3


def get_result(n):
    i = get_untidy_index(n)
    if i < 0:
        return n
    middle = str(int(n[i]) - 1)
    end = '9' * (len(n) - i - 1)
    return str(int(n[:i] + middle + end))

def get_untidy_index(n):
    last = 0
    last_i = 0
    for i, digit in enumerate(n):
        digit = int(digit)
        if digit > last:
            last_i = i
            last = digit
        elif digit < last:
            return last_i
    return -1


results = []
with open('large1.in') as input_file:
    with open('large1.out', 'w') as output_file:
        T = int(input_file.readline())

        for i in range(T):
            n = str(int(input_file.readline()))
            result = get_result(n)
            output_file.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
