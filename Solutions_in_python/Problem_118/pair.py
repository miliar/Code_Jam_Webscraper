import sys, math

def isPalindrome(num):
    n = num
    rev = 0
    while (num > 0):
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;

    return rev == n

def checkValue(start, end):
    start = int(math.ceil(math.sqrt(start)))
    end = int(math.sqrt(end))

    count = 0
    for i in xrange(start, end+1):
        k = i * i;
        if (k < 10):
            count = count + 1
        elif i > 10 and i < 100:
            if i is 11 or i is 22:
                count = count + 1
        else:
            if (isPalindrome(i) == True and isPalindrome(k) == True):
                count = count + 1
    
    return count

if __name__ == '__main__':
    lines = int(raw_input())
    for i in xrange(lines):
        line = raw_input()
        argu = line.split()

        print "Case #%s: %s"%(i+1, checkValue(int(argu[0]), int(argu[1])))
