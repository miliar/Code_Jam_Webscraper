def int_to_list(n):
    l = []
    while n > 9:
        l.append(n%10)
        n = n/10
    l.append(n)
    return l[::-1]

def list_to_int(l):
    n = 0
    for num in l:
        n = 10*n + num
    return n

T = int(raw_input())
for i in xrange(1, T+1):
    N = int(raw_input())
    digits = int_to_list(N)
    j = 0
    while j < len(digits) - 1:
        if digits[j] <= digits[j+1]:
            j += 1
        else:
            digits[j] -= 1
            while j > 0 and digits[j] < digits[j-1]:
                j -= 1
                digits[j] -= 1
            j += 1
            while j < len(digits):
                digits[j] = 9
                j += 1
            break
    result = list_to_int(digits)
    print "Case #{}: {}".format(i, result)
    