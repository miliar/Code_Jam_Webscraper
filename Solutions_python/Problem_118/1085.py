import math

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def check_palindrome(i):
    i = str(i)
    if i == i[::-1]:
        return True
    return False


def get_fns(a, b):
    output = []
    for i in range(a, b+1):
        if check_palindrome(i):
            if is_square(i) and check_palindrome(int(i ** .5)):
                output.append(i)
    return output
        

def read_input():
    no_of_cases = input()
    for i in range(no_of_cases):
        a, b = map(int, raw_input().split(' '))
        print "Case #%d: %d" % (i+1, len(get_fns(a, b)))


if __name__ == '__main__':
    read_input()
