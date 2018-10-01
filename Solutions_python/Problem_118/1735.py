import math

def main():
    numberOfCases = int(raw_input())
    for x in range (1,numberOfCases+1):
        a,b = raw_input().split()
        a,b = int(a),int(b)
        sqrtA = math.ceil(math.sqrt(a))
        sqrtB = math.floor(math.sqrt(b))
        results = 0
        #print "case {0}".format(x)
        #print "sqrta {0}, sqrtb {1}".format(int(sqrtA), int(sqrtB))
        for i in range(int(sqrtA), int(sqrtB)+1):
            if isPalindrome(i) and isPalindrome(i*i):
                results = results + 1
        print "Case #{0}: {1}".format(x,results)


def isPalindrome(number):
    rev = 0
    org = number
    while number > 0:
        last = number % 10
        rev = rev * 10 + last
        number = number / 10

    return org == rev

if __name__ == "__main__":
    main()
