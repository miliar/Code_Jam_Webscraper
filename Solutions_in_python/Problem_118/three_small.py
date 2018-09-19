import argparse
import math

N = (2, 4, 8, 10, 14, 18, 20, 24, 30, 38, 40)

palindromic_squares = set()


def read_input(input_file):
    number_of_test_cases = input_file.readline()
    for i in xrange(1, int(number_of_test_cases) + 1):
        data = ''
        data = input_file.readline().strip('\n')
        q = compute(data)
        print 'Case #%d: %s' % (i, q)


def compute(data):
    count = 0
    interval = data.split(' ')
    for i in xrange(int(interval[0]), int(interval[1]) + 1):
        if is_palindromic_square(i):
            palindromic_squares.add(i)
            count += 1
    return count


def is_palindromic_square(n):
    is_ps = False
    if len(str(n)) not in N and is_palindromic(n):
        res = is_perfect_square(n)
        if res[0] and is_palindromic(res[1]):
            is_ps = True
    return is_ps


def is_palindromic(n):
    return str(n) == str(n)[::-1]


def is_perfect_square(n):
    root = math.sqrt(n)
    int_root = int(root)
    return int_root == root, int_root


def two(input_file):
    read_input(input_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=file)
    args = parser.parse_args()
    two(args.input_file)
