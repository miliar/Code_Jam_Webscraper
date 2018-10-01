def solve(filecontent):
    lines = filecontent.splitlines()
    T = int(lines[0])
    out = []
    for tcase in xrange(1,T+1):
        line = lines[tcase].split(" ")
        N = int(line[0])
        K = int(line[1])
        tcaseOut = ("Case #%d: " % (tcase,))
        if K & ((1<<N) - 1) == ((1<<N) - 1):
            tcaseOut += "ON"
        else:
            tcaseOut += "OFF"
        out.append(tcaseOut)
    return "\n".join(out)

f = file("codejam/A-large.in").read()
file("codejam/A-large.out",'w').write(solve(f))
