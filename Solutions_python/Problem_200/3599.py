def is_tidy(s):
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return False
    return True


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        for j in xrange(n, 0, -1):
            s = str(j)
            if is_tidy(s):
                print "Case #{}: {}".format(i, s)
                break