import math
cases = int(input())

def is_palindrome(x):
    str_x = str(x)
    if len(str_x) % 2:
        left = len(str_x) / 2
        right = len(str_x) / 2 + 1
    else:
        right = left = len(str_x) / 2
    if str_x[:left] == str_x[right:]:
        return True
    return False


index = 1
while index <= cases:
    s = raw_input()
    left_end, right_end = s.split()
    left_min = math.sqrt(int(left_end))
    if left_min > int(left_min):
        left_min = int(left_min) + 1
    else:
        left_min = int(left_min)
    right_min = int(math.sqrt(int(right_end)))
    numbers = 0
    i = left_min
    while i <= right_min:
        if is_palindrome(i) and is_palindrome(i*i):
            numbers += 1
        i += 1
    print "Case #%d: %d" % (index, numbers)
    index += 1
