import sys
import math

def reverseNumber(number):
    result = number % 10
    number /= 10
    while number > 0:
        result = number % 10 + result * 10
        number /= 10
    return result

# Read input file
f = open(sys.argv[1], 'r')
lines = f.readlines()

# Read number of cases
T = int(lines[0].rstrip())
li = 0

# Process cases
for t in range(T):
    li += 1
    line = lines[li].rstrip().split(' ')
    A = int(line[0])
    B = int(line[1])
    a = int(math.ceil(math.sqrt(A)))
    b = int(math.floor(math.sqrt(B)))
    result = 0
    for i in range(a, b+1):
        if i == reverseNumber(i) and i**2 == reverseNumber(i**2):
            result += 1
    print("Case #{0}: {1}".format(t+1, result))
