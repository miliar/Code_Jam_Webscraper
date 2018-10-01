def tidy(num):
    chrs = str(num)
    while (True):

        pos = 0
        prev_digit = None
        break_pos = None
        while pos < len(chrs):
            digit = chrs[pos]
            if prev_digit is not None and digit < prev_digit:
                break_pos = pos
                break
            prev_digit = digit
            pos += 1

        if break_pos is not None:
            start = int(chrs[0:break_pos + 1])
            start -= (start % 10) + 1
            end = '9' * ((len(chrs) - break_pos) - 1)
            num = int(str(start) + end)
            chrs = str(num)
        else:
            break
    return num

if __name__ == '__main__':
    with open('B-large.in', 'r') as f:
        next(f)
        x = 0
        for l in f:
            x +=  1
            num = int(l)
            print "Case #" + str(x) + ": " + str(tidy(num))
