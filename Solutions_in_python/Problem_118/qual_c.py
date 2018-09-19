import sys

# based on https://en.wikipedia.org/wiki/Isqrt
def isqrt(n):
    x = n
    y = (x + n//x)//2
    while abs(y-x) > 1:
        x = y
        y = (x+n//x)//2
    return y

def is_pal(n):
    x = n
    reversed = 0
    while x > 0:
        x, d = divmod(x, 10)
        reversed = reversed * 10 + d;

    return n == reversed

sys.stdin.readline()

case = 1
for line in sys.stdin:
    (a,b) = [int(x) for x in line.split()]
    count = 0
    i = isqrt(a)
    square = i**2
    while square <= b:
        if square >= a and square <= b and is_pal(i) and is_pal(square):
            count += 1
        i += 1
        square = i**2

    print('Case #{}: {}'.format(case, count))
    case += 1
