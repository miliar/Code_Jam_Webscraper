# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

fo = open("q2input.txt", "r")
t = int(fo.readline())
for i in xrange(1, t + 1):
    nums = fo.readline().split(" ")  # read a list of integers, 2 in this case
    digits = []
    num = int(nums[0])

    for l in xrange(0,19):
        digit = num % 10
        digits.append(digit)
        num = (num - digit)/10
        if (num < 1):
            break

    prev_digit = digits[0]
    digits = list(reversed(digits))
    start = len(digits)
    for j in xrange (0, len(digits) - 1):
        if (digits[j] == digits[j+1]):
            start = min(start, j)
        if (digits[j] > digits[j+1]):
            start = min(start, j)
            digits[start] = digits[start] - 1
            for k in xrange(start+1,len(digits)):
                digits[k] = 9
            break

    if (digits[0] == 0):
        digits[0] = ""

    out = "".join(str(d) for d in digits)
    # output number
    print "Case #{}: {}".format(i, out)
