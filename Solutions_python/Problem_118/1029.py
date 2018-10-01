import math
filename = "C-small-attempt1.in"
input_file = open(filename, 'r')

def is_palindrome(n):
    a = 0
    b = n
    while(b > 0):
        a = a * 10 + b % 10
        b /= 10
    if a == n:
        return True
    else:
        return False

case = int(input_file.readline())
A = 0
B = 0
for n in range(case):
    count = 0
    interval = input_file.readline().split(' ')
    A = int(interval[0])
    B = int(interval[1])
    #print A, B
    for i in range(int(math.sqrt(A)), int(math.sqrt(B)+1)):
        if i ** 2 < A or i ** 2 > B:
            continue
        if is_palindrome(i) and is_palindrome(i ** 2):
            #print i ** 2
            count += 1
    print "Case #" + str(n+1) + ": " + str(count)

input_file.close()
