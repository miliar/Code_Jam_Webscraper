import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-22s %(levelname)-8s %(message)s')

# Test function
def is_tidy(n):
    last_digit = -1
    for _digit in str(n):
        digit = int(_digit)

        if last_digit != -1:
            if last_digit > digit:
                return False

        last_digit = digit

    return True

# Testcases
assert is_tidy(0)
assert is_tidy(8)
assert is_tidy(123)
assert is_tidy(555)
assert is_tidy(224488)
assert not is_tidy(20)
assert not is_tidy(321)
assert not is_tidy(495)
assert not is_tidy(999990)

# Find last tidy number
def find_last_tidy(n):

    i = n
    while True:
        if is_tidy(i):
            return i

        # The trick is simply to take 'safe' big steps
        # we can simply move entire orders of magnitude
        # downwards by finding the next suitable number
        # that can realistically yield a tidy number,
        # which we can base on powers of 10.
        for j in range(20, 10, -1):
            remainder = i % (10 ** j)
            if remainder > 0 and remainder != i:
                logging.debug("-{}".format(remainder))
                i -= remainder
                break

        i -= 1
        logging.debug("-1")

assert find_last_tidy(132) == 129
assert find_last_tidy(1000) == 999
assert find_last_tidy(7) == 7
assert find_last_tidy(111111111111111110) == 99999999999999999

with open("B-small-attempt0.in", "r") as f:
    cases = int(f.readline())

    case = 1
    for n_str in f:
        print("Case #{}: {}".format(case, find_last_tidy(int(n_str))))
        case += 1
        if case > cases:
            break
