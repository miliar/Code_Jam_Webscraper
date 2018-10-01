import sys, math, numbers
input = open(sys.argv[1], 'r')

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def getSquare(num):
    res = math.sqrt(num)
    return int(res) if res.is_integer() else None

for i in range(int(input.readline())):
    lower, upper = [int(x) for x in input.readline().split(' ')]

    # get closest square root
    closest_root = 1
    while closest_root*closest_root < lower:
        closest_root += 1

    counter = 0
    root = closest_root
    while True:
        squared = root * root
        if not lower <= squared <= upper:
            break
        elif isPalindrome(root) and isPalindrome(squared):
            counter += 1
        root += 1


    print('Case #{}: {}'.format(i+1, counter))
