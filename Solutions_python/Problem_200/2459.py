def solve(num):
    j = len(num)
    for i in xrange(len(num) - 1, 0, -1):
        if num[i - 1] > num[i]:
            j = i
            num = num[:j - 1] + str(int(num[j - 1]) - 1) + '9' * (len(num) - j)
    res = num
    if num[0] == '0':
        return res[1:]
    return res


def main():
    n = input()
    for i in xrange(n):
        inp = raw_input()
        print "Case #" + str(i + 1) + ": " + solve(inp)


main()