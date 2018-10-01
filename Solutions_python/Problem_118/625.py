import sys

FILE_NAME = 'C-large-1'

f_in = open(FILE_NAME + '.in', 'r')
f_out = open(FILE_NAME + '.out', 'w')

# Read the number of tests
T = int(f_in.readline())

ends = ['1', '4', '5', '6', '9']
lens = [2, 4, 8, 10, 14, 18, 20, 24, 30, 38, 40]

# Ger the next palindrome
def next(n):
    l = len(str(n))

    odd = (l % 2 != 0)
    
    left = str(n)[:len(str(n)) / 2]
    middle = str(n)[(len(str(n)) - 1) / 2]
    
    if odd:
        inc = pow(10, l / 2)
        new = int(left + middle + left[::-1])
    else:
        inc = int(1.1 * pow(10, l / 2))
        new = int(left + left[::-1])
    
    if new > n:
        return new
    if middle != '9':
        return new + inc
    else:
        return next(round(n))

# Round the number up
def round(n):
    l = len(str(n))
    inc = pow(10, ((l / 2) + 1))
    return ((n / inc) + 1) * inc


# Precalculate 10 ^ 4 (10 ^ 15 just in case)
palin = list()

A, B = 1, pow(10, 15)

n = int(pow(A, 0.5)) - 1
p = 0

while (p <= B):
    n = next(n)
    p = pow(n, 2)
    s = str(p)
    if s[-1:] in ends: 
        if not len(s) in lens:
            if s == s[::-1] and p >= A and p <= B: 
                palin.append(p)
                n = int(pow(next(p), 0.5))

# For each test...

for t in range(T):

    # Read the A and B
    A, B = map(int, f_in.readline().split())

    result = len(filter(lambda x:  x >= A and x <= B, palin))

    # Write the output
    f_out.write("Case #" + str(t + 1) + ": " + str(result))

    if t + 1 < T: f_out.write("\n")

f_out.close()
f_in.close()