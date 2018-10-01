import re, sys

def recy(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    str1 = str1[1:] + str1[0]
    for i in xrange(1, len(str1)):
        if (str1 == str2):
            return True
        else:
            str1 = str1[1:] + str1[0]
    
    return False

def coreCalc(data):
    a = data[0]
    b = data[1]
    result = 0
    for i in xrange(a, b):
        for j in xrange(b, i, -1):
            if (recy(i, j)):
                result += 1
    return result

N = int(sys.stdin.readline().strip())
for qw in range(1, N + 1):
    print 'Case #%d:' % qw,

    data = [int(i) for i in sys.stdin.readline().strip().split()]
    result = coreCalc(data)
    print result
