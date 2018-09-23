def choose_bathroom(n,m):

    i = 0
    p = 0

    while True:

        p = 2 ** i
        if p >= m: break
        i += 1

    if p > m:
        i -= 1
        p = 2 ** i

    r = n - p + 1
    area = n//p
    gone = m - p + 1

    count_ls = r%p
    count_rs = p - count_ls

    if gone > count_ls and count_ls > 0:
        area -= 1

    ls = area//2
    rs = area - ls - 1

    return max(ls,rs),min(ls,rs)

if __name__ == '__main__':
    i = 0
    n = 0
    tc = 0
    inp = open('C-large.in.txt',"r")
    out = open('C-large.out.txt',"w")
    for line in inp:
        if i == 0:
            tc = int(line.strip())
        else:
            if i <= tc:
                vals = line.strip().split()
                n = int(vals[0])
                m = int(vals[1])
                v1,v2 = choose_bathroom(n,m)
                s = str("Case #"+str(i)+": "+str(v1)+" "+str(v2)+"\n")
                out.write(s)
        i += 1
