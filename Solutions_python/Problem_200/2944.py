import string

def DigitToIncrease(n):
    reverse_digit_indices = range(1, len(n))
    reverse_digit_indices.reverse()
    for i in reverse_digit_indices:
        if int(n[i - 1]) > int(n[i]):
            while i != len(n) - 1 and n[i] == n[i + 1]:
                i += 1
            return i
    return -1

def SetCharacter(string, index, value):
    result = string[:index] + value + string[index + 1:]
    return result

def AnyAtLeastAsSignificantDigitHasBeenDecreased(has_been_decreased, index):
    for i in range(0, index + 1):
        if has_been_decreased[i]:
            return True
    return False

def IncreaseDigit(n, digit_to_increase, has_been_decreased):
    n = SetCharacter(n, digit_to_increase, "9")
    i = digit_to_increase - 1
    while i >= 0:
        if n[i] == "0":
            n = SetCharacter(n, i, "9")
            i -= 1
        else:
            if not AnyAtLeastAsSignificantDigitHasBeenDecreased(has_been_decreased, i):
                n = SetCharacter(n, i, str(int(n[i]) - 1))
                has_been_decreased[i] = True
            break
    return n

def RemoveLeadingZeroes(n):
    while n[0] == "0":
        n = n[1:]
    return n

def Solve(n):
    has_been_decreased = [False for c in n]
    while True:
        digit_to_increase = DigitToIncrease(n)
        if digit_to_increase == -1:
            break
        n = IncreaseDigit(n, digit_to_increase, has_been_decreased)
    return RemoveLeadingZeroes(n)

num_cases = int(raw_input())
for case_num in xrange(1, num_cases + 1):
    n = raw_input()
    solution = Solve(n)
    print "Case #{}: {}".format(case_num, solution)