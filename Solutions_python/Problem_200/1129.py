import sys

chars = dict({'-': '+', '+': '-'})

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def find_first_lowest(num):
    digits = str(num)
    length = len(digits)
    for index in range(0, length - 1):
        if ord(digits[index]) > ord(digits[index + 1]):
            return index + 1
    return -1


assert find_first_lowest(1234) == -1
assert find_first_lowest(4321) == 1
assert find_first_lowest(3332) == 3
assert find_first_lowest(3339) == -1
assert find_first_lowest(9339) == 1
assert find_first_lowest(132) == 2
assert find_first_lowest(1000) == 1
assert find_first_lowest(7) == -1
assert find_first_lowest(1430) == 2
assert find_first_lowest(999) == -1
assert find_first_lowest(332) == 2
assert find_first_lowest(1880) == 3
assert find_first_lowest(1900) == 2

def is_tidy(num):
    return find_first_lowest(num) == -1

assert is_tidy(1234) == True
assert is_tidy(4321) == False
assert is_tidy(3332) == False
assert is_tidy(3339) == True

def are_same_digits(num):
    digits = str(num)
    length = len(digits)
    for index in range(1, length):
        if digits[index] != digits[0]:
            return False
    return True

assert are_same_digits(111) == True
assert are_same_digits(112) == False
assert are_same_digits(121) == False
assert are_same_digits(211) == False

def minus_prefix(num):
    prefix = str(num)
    result = prefix[0]
    length = len(prefix)
    for index in range(1, length):
        result += '0'
    return int(result)

assert minus_prefix(999) == 900
assert minus_prefix(111) == 100
assert minus_prefix(55555) == 50000

def find_result(num):
    # print(" ---- num", num)
    if is_tidy(num) is True:
        return num
    answer = num
    snum = str(num)
    lowest_index = find_first_lowest(num)
    # print("num", num, "lowest_index", lowest_index)
    if lowest_index == -1:
        return num
    if snum[lowest_index] == '0':
        prefix = snum[0:lowest_index]
        if are_same_digits(int(prefix)) is True:
            prefix = minus_prefix(int(prefix))
        result = int(prefix) - 1
        if is_tidy(result) is False:
            result = find_result(result)
        suffix = '9' * (len(snum) - lowest_index)
        # print("IS ZERO num", num, "prefix", prefix, "result", result, "suffix", suffix)
        answer = str(result) + suffix
    else:
        prefix = snum[0:lowest_index]
        result = int(prefix) - 1
        if is_tidy(result) is False:
            result = find_result(result)
        suffix = '9' * (len(snum) - lowest_index)
        # print("NOT ZERO num", num, "prefix", prefix, "result", result, "suffix", suffix)
        answer = str(result) + suffix
    return int(answer)

def solve(num):
    return find_result(int(num))

assert solve(89909) == 88999
assert solve(132) == 129
assert solve(111111111111111110) == 99999999999999999

lines = get_lines()
nb_cases = int(lines.pop(0))

for case in range(0, nb_cases):
    snum = lines.pop(0)
    answer = solve(snum)
    print("Case #", (case + 1), ": ", answer, sep="")
