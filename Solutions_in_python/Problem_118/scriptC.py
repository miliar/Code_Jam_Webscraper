import sys
import math

if len(sys.argv) != 3:
    print("Usage: python scriptC.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'sampleC.in'
#output_file = 'sampleC.out'

def palindrom_check(n):
    ndigits = long(math.log10(n)) + 1
    if ndigits == 1:
        return 1
    elif ndigits == 2:
        if n % 10 == n / 10:
            return 1
    else:
        temp = (10 ** (ndigits - 1))
        if n % 10 == n / temp:
            return palindrom_check((n % temp) / 10)
    return 0

def palindrom_generator(num_digits):
    if num_digits == 1:
        for i in xrange(1,10):
            yield i
    elif num_digits == 2:
        for i in xrange(1,10):
            yield i * 10 + i
    else:
        for i in xrange(1,10):
            for j in palindrom_generator(num_digits - 2):
                yield j * 10 + i + i * (10 ** (num_digits - 1))


def palindroms_in_range(l, r):
    ldigits = long(math.log10(l)) + 1
    rdigits = long(math.log10(r)) + 1
    for num_digits in xrange(ldigits, rdigits + 1):
        for palindrom in palindrom_generator(num_digits):
            if palindrom >= l and palindrom <=r:
                yield palindrom

def fair_and_square_in_range(A, B):
    l = long(math.ceil(math.sqrt(A)))
    r = long(math.floor(math.sqrt(B)))
    for d in palindroms_in_range(l, r):
        d_squared = d ** 2
        if palindrom_check(d_squared):
            yield d_squared

def check_range(A,B):
    cnt = 0
    for i in fair_and_square_in_range(A, B):
        cnt += 1
    return cnt

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for c in xrange(0,T):
        line = f.readline()
        A, B = tuple(map(long, line.split(' ')))
        num = check_range(A, B);
        results.append('Case #' + str(c+1) + ': ' + str(num) + '\n')

with open(output_file, 'w') as f:
        f.writelines(results)



