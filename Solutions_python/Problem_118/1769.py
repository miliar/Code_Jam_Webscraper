import cj
import math

cases = cj.parse_cases(cj.ifile(), 1)

def isPalindrome(num):
    numString = str(num)
    rev = numString[::-1]
    
    return (numString == rev)

def solve(case):
    line, = case
    limits = line.split(' ')

    lower = long(limits[0])
    upper = long(limits[1])

    lowerRoot = long(math.ceil(math.sqrt(lower)))
    upperRoot = long(math.floor(math.sqrt(upper)))

    count = 0

    # print "lower root %s upper %s" % (lowerRoot, upperRoot)

    for i in range(lowerRoot, upperRoot + 1):
        if isPalindrome(i):
            if isPalindrome(i * i):
                count = count + 1

    return str(count)

answers = [solve(c) for c in cases]
cj.print_answers(answers)
