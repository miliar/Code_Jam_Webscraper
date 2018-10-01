def get_largest_befores(digits):
    ret = [0]
    for i in range(len(digits) - 1):
        ret.append(max(digits[i], ret[i]))
    return ret

def last_tidy_number(digits):
#     answer = digits
    n = len(digits)
    largest_befores = get_largest_befores(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < largest_befores[i]:
            for j in range(i, n):
                digits[j] = 9
            digits[i - 1] -= 1

    return int(''.join([str(d) for d in digits]))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
#     inp = raw_input().split(" ")
    digits = [int(d) for d in list(raw_input())]
    print "Case #{}: {}".format(i, last_tidy_number(digits))
