import numpy as np

with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def is_tidy(x):
    for i in xrange(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return True


def ge_digits(d1, d2):
    d1_int = int(''.join(map(str, d1)))
    d2_int = int(''.join(map(str, d2)))
    if d1_int > d2_int:
        return True


def count_tidy(digits):
    if is_tidy(digits):
        return int(''.join([str(d) for d in digits]))
    else:
        new_digits = list(digits)
        for i in xrange(len(digits) - 1, -1, -1):
            if is_tidy(new_digits):
                if ge_digits(new_digits, digits):
                    new_digits[i] -= 1
                    if not is_tidy(new_digits):
                        new_digits[i] = 9
            else:
                new_digits[i] = 9
        return int(''.join([str(d) for d in new_digits]))


f = open('out.txt', 'w')
for i in xrange(1, t + 1):
    n = int(lines[i])
    print n
    digits = list(str(n))
    digits = [int(d) for d in digits]
    ans = count_tidy(digits)
    print('Case #%s: %s \n' % (i, ans))
    f.write('Case #%s: %s \n' % (i, ans))
f.close()
