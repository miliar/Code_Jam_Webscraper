def last_tidy_index(n):
    curr = '0'
    chars = list(str(n))
    for i, c in enumerate(chars):
        if curr > c:
            return i - 1
        else:
            curr = c
    return len(chars)




if __name__ == '__main__':
    import sys
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        chars = sys.stdin.readline().strip()
        ind = last_tidy_index(chars)

        report = lambda x: print('Case #%d: %s' % (i, x))

        if ind == (len(chars)):
            report(chars)
        elif chars[ind] == '1':
            report(''.rjust(len(chars) - 1, '9'))
        else:
            digit_ind = chars.index(chars[ind])
            report((chars[:digit_ind] + str(int(chars[digit_ind]) - 1)).ljust(len(chars), '9'))
