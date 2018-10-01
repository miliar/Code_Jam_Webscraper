from sys import argv
import math

#f = open(sys.argv[1])
f = open("C-small-attempt0.in")
cases = int(f.readline())


def checkPalindrome(in_num):
    str_num = str(in_num)
    start = 0
    end = len(str_num)-1
    while start < end and str_num[start] == str_num[end]:
        start += 1
        end -= 1
    return end <= start
    

for i in range(cases):
    count = 0
    L, U = map(int, f.readline().split())
    sqrt_num = int((math.ceil(math.sqrt(L))))
    num = sqrt_num**2
    while num <= U:
        if checkPalindrome(sqrt_num) and checkPalindrome(num):
            count += 1
        sqrt_num += 1    
        num = sqrt_num**2    

    print "Case #%d:" % (i + 1), count

f.close()
    
