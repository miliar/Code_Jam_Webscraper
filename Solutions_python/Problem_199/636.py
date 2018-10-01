def flip(str, beg, k):
    if beg == len(str): return 0, str
    if(len(str)-beg < k): return -1, str
    if(len(str)-beg == k):
        if str[beg:beg+k] == '-'*k:
            str = str[:beg] + '+'*k
            return beg+k, str
        else:
            return -1, str
    new_beg = beg
    for i in range(k):
        if str[beg+i] == '-':
            str = '%s+%s' % (str[:beg+i], str[beg+i+1:])
        else:
            str = '%s-%s' % (str[:beg + i], str[beg + i + 1:])
            if(new_beg == beg):
                new_beg = beg+i
    if(new_beg == beg): new_beg = beg+k
    return new_beg, str

with open("A-large.out", 'w') as output:
    with open("A-large.in", "r") as input:
        n = int(input.readline(-1).strip())
        for i in range(n):
            line = input.readline(-1).split()
            str = line[0]
            k = int(line[1].strip())
            beg = 0
            n = 0
            while(beg != len(str)):
                while(beg < len(str) and str[beg] != '-'):
                    beg += 1
                tmp, str = flip(str, beg, k)
                if tmp == -1:
                    break
                if tmp != 0:
                    beg = tmp
                    n += 1
            if tmp == -1:
                output.write("Case #%d: IMPOSSIBLE\n" % (i+1))
                continue
            output.write("Case #%d: %d\n" % (i+1, n))



