
"""
Google code jam solutions
Shaul Garbuz
"""

"""
Problem A: Oversized Pancake Flipper
"""

IMPOSSIBLE = 'IMPOSSIBLE'

def parse_pancake_case(s):
    return [1 if a == '+' else 0 for a in s]

def flip(s, start, end):
    s[start : end] = [int(not f) for f in s[start : end]]
    return s

def flip_pancakes(s, k, case):
    s = parse_pancake_case(s)
    flips = 0
    n = len(s)
    for i in range(n - k + 1):
        if s[i] == 0:
            s = flip(s, i, i + k)
            flips += 1
    res = flips if sum(s) == n else IMPOSSIBLE
    return 'Case #{}:\t{}'.format(case + 1, res)

def flip_pancakes_file(path):
    with open(path, 'rb') as f:
        content = f.readlines()[1 : ]
        results = []
        for case, line in enumerate(content):
            s, k = line.split()
            results.append(flip_pancakes(s, int(k), case))
        with open('{}.out'.format(path), 'wb') as f:
            f.write("\n".join(results))

"""
Problem B: Tidy Numbers
"""

def to_digits(number):
    return map(int, str(number))

def to_number(digits):
    return int(''.join(map(str, digits)))

def largest_tidy_number(n, case):
    digits = to_digits(n)
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            digits = digits[ : i] + [9] * (len(digits) - i)
            reduction = 10 ** (len(digits) - i)
            digits = to_digits(to_number(digits) - reduction)
    return 'Case #{}:\t{}'.format(case + 1, to_number(digits))

def tidy_file(path):
    with open(path, 'rb') as f:
        content = f.readlines()[1 : ]
        results = '\n'.join([largest_tidy_number(int(d), i) for i, d in enumerate(content)])
        with open('{}.out'.format(path), 'wb') as f:
            f.write(results)

def main():
    tidy_file('/Users/Shaul/Desktop/B-large.in')

if __name__ == '__main__':
    main()