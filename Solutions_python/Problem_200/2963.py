__author__ = 'wwang'

def is_tidy(num):
    last_digit = 0
    for digit in list(str(num)):
        if int(digit) < last_digit:
            return False
        last_digit = int(digit)
    return True


t = int(input())  # read a line with a single integer
for ii in range(1, t + 1):
    input_num = int(input())

    for i in reversed(range(input_num + 1)):
        if is_tidy(i):
            print("Case #%d: %d" % (ii, i))
            break
