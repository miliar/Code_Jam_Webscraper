import math


def check_palindrome(x):
    s = str(x)
    arr = []
    for c in s:
        arr.append(c)

    arr2 = []
    for c in reversed(arr):
        arr2.append(c)

    if arr == arr2:
        return True

    return False


def check_square(n):

    if n == 1:
        return True

    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False

line_number = 0
arr = []

with open('C-small-attempt5.in.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        if line_number > 0:
            bounds = a_line.rstrip().split(" ")
            lower_bound = int(bounds[0])
            upper_bound = int(bounds[1])

            count = 0

            for r in range(lower_bound, upper_bound + 1):
                if check_palindrome(r) and check_square(r):
                    if check_palindrome(int(math.sqrt(r))):
                        count += 1

            arr.append("Case #{0}: {1}".format(line_number, count))

        line_number += 1

s = "\n".join(arr)

with open('b.out', mode='w', encoding='utf-8') as a_file:
    a_file.write(s)