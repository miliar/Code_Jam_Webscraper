"none"
import fileinput

def test_tidy():
    "none"
    assert is_tidy(123) is True
    assert is_tidy(321) == 1
    assert is_tidy(1000) == 1
    assert is_tidy(1200) == 2
    assert fill_zeros(1200, is_tidy(1200)) == 1200
    assert fill_zeros(321, is_tidy(321)) == 300
    assert fill_zeros(132, is_tidy(132)) == 130

def fill_zeros(num, pos):
    "none"
    str_num = list(str(num))
    str_num[pos:] = '0' * (len(str_num) - pos)
    return int(''.join(str_num))

def is_tidy(num):
    "none"
    last_char = 0
    for pos, char in enumerate(str(num)):
        if char < last_char:
            return pos
        last_char = char
    return True

def solve_simple(num):
    "none"
    while num > 0:
        if is_tidy(num) is True:
            return num
        num -= 1
    return 1

def solve(num):
    while num > 0:
        pos = is_tidy(num)
        if pos is True:
            return num
        num = fill_zeros(num, pos) - 1
    return 1

test_tidy()

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    N = map(int, line.strip().split(" "))[0]
    res = solve(N)
    if res is None:
        res = "IMPOSSIBLE"
    print "Case #%d: %s" % (i, res)

