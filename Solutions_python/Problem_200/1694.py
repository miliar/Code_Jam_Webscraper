import math

def is_tidy(num):
    num_str = str(num)
    for i in range(len(num_str)-1):
        if num_str[i] > num_str[i+1]:
            return False
    return True


def find_tidy(num):
    tidy = is_tidy(num)

    while not tidy:
        num -= 1
        tidy = is_tidy(num)

    return num

def find_tidy_2(num):
    str_num = str(num)
    if is_tidy(num):
        return num
    else:
        digits = int(math.log10(num))+1
        first_digit = int(str_num[0])
        if num < int(str(int(first_digit))*digits):
            if first_digit > 1:
                return find_tidy_2(int(str(first_digit-1) + '9'*(digits - 1)))
            else:
                return find_tidy_2('9'*(digits-1))
        else:
            return int(str_num[0] + str(find_tidy_2(int(str_num[1:]))))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print('Case #{}: {}'.format(i, find_tidy_2(n)))
    