


def check_tidy(n):
    n = str(n)
    m = sorted(n)
    m = ''.join(m)
    if n == m:
        return True
    else:
        return False

def main(n):
    idx = -1
    flag = check_tidy(n)
    if flag:
        return n
    while True:
        strn = str(n)
        try:
            if strn[idx-1] == strn[idx-2]:
                strn = strn[:idx-1] + '0' + strn[idx:]
                n = int(strn)
                idx -= 1
            else:
                break
        except:
            break
    while True:
        flag = check_tidy(n)
        if flag:
            return n
        else:
            n -= 1

def io(inp, out):
    f = open(inp, 'r')
    out = open(out, 'w')
    n = int(f.readline())
    for i in xrange(n):
        l = f.readline()
        out.write('Case #%d: ' %(i+1))
        ans = main(int(l))
        out.write(str(ans) + '\n')

io('B-small-attempt0.in', 'b_small_ans.txt')

