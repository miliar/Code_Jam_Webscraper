def is_tidy(n):
    for i, num in enumerate(n[:-1]):
        if int(num) > int(n[i+1]):
            return i
    return -1

def solve(num):
    if len(num) == 1:
        return num

    tindex = is_tidy(num)
    if tindex == -1:
        return num

    untidy = num[tindex:]

    tidy = num[:tindex] + str(int(untidy[0]) - 1) + '9'*(len(untidy)-1)
    return solve(tidy)

def run(ip, op):
    t = int(ip.readline().replace('\n', ''))
    line = ip.readline().replace('\n', '')
    for i in xrange(t):
        s = line
        sol = solve(s)
        op.write('Case #%d: %d\n' % (i+1, int(sol)))

        line = ip.readline().replace('\n', '')

if __name__ == "__main__":
    import sys
    fp = sys.argv[1]
    fpo = fp + '.out'
    rh = open(fp, 'r')
    wh = open(fpo, 'w')
    run(rh, wh)
    rh.close()
    wh.close()
