import sys
import math

def palindrome(number):
    digits = str(number)

    for i in range(len(digits)//2):
        if digits[i] != digits[len(digits)-1-i]:
            return False

    return True

def is_fair_and_square(number):
    if palindrome(number) == False:
        return False
    else:
        number = math.sqrt(number)
        if math.modf(number)[0] != 0.0:
            return False
        else:
            number = int(number)
            if palindrome(number) == False:
                return False
            else:
                return True

if __name__ == '__main__':
    f = open(sys.argv[1])
    lines_num = int(f.readline())
    for x in range(lines_num):
        a, b = [int(x) for x in f.readline().split()]

        palindromes = 0
        for i in range(a,b+1):
            if is_fair_and_square(i):
                palindromes += 1

        print("Case #%d: %d" % (x + 1, palindromes))

