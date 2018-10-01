def dance(n, s, p, totals):
    res = 0
    for total in totals:
        a = b = c = total/3
        sum = a + b + c
        if sum == total-1 and a < 10:
            a = a+1
        elif sum == total-2 and a < 10 and b < 10:
            a = a+1
            b = b+1

        if a == p-1 and s > 0 and a == b and a < 10 and b > 0:
            s = s-1
            a = a+1
            b = b-1

        if a >= p:
            res += 1
    return res

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        line = map(int, raw_input().split(' '))
        res = dance(line[0], line[1], line[2], line[3:])
        print "Case #%d: %d" % (i+1, res)
