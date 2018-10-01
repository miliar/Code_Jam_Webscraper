cases = int(input())


def lock_digit(n,l):
    prev = 0
    number = int('1' * l)
    for i in range(10):
        if i * number <= n:
            prev = i
        else:
            return prev
    return prev


def run_case(max):
    num = str(max)
    n = num
    result = ""
    l = len(n)
    for c in num:
        digit = lock_digit(int(n),l)
        if digit >= int(n[:len(n)-l + 1]):
            n = n[1:]
        l -= 1
        result += str(digit)
    return str(int(result))




for c in range(cases):
    print("Case #" + str(c+1) + ": " + run_case(int(input())))