def solver(instr):
    n, dline=instr.split(' ')
    n = int(n)
    dline = map(int,list(dline))
    res, cur = 0, dline[0]
    for i in range(1,n+1):
        if cur<i:
            res+=(i-cur)
            cur = i
        cur += dline[i]
    return res

with open("1.in",'r') as infile:
    lines=infile.readlines()
with open("1.out",'w') as outfile:
    for i in range(1,len(lines)):
        outfile.write("Case #%d: %d\n" %(i, solver(lines[i].strip())))
