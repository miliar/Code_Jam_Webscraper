def unique(s):
    res = []
    prev = -1
    for c in s:
        if c != prev:
            res.append(c)
        prev = c
    res = ''.join(res)
    return res

def counts(s):
    res = []
    prev = s[0]
    val = 0
    for c in s:
        if c != prev:
            res.append(val)
            val = 1
        else:
            val += 1
        prev = c
    if val > 0:
        res.append(val)
    return res

def do_case(case_num, ss):
    if unique(ss[0]) != unique(ss[1]):
        print "Case #%d: Fegla Won" % case_num
    else:
        s = 0
        c0 = counts(ss[0])
        c1 = counts(ss[1])
        for i in range(len(c1)):
            s += abs(c0[i] - c1[i])
        print "Case #%d: %d" % (case_num, s)
    
def main():
    T = int(raw_input())
    for case_num in range(1, T + 1):
        n = int(raw_input())
        ss = []
        for i in range(n):
            s = raw_input().strip()
            ss.append(s)
        do_case(case_num, ss)

if __name__ == "__main__":
    main()
