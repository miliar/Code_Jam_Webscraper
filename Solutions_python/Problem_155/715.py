f = open("a.in", "rU")

def ri():#int
    return int(f.readline().strip())
def rl(sep=False):#list of string
    if not sep:
        return f.readline().split()
    return f.readline().split(sep)
def rt(sep=False):#tuple of string
    return tuple(rl(sep))

cases = ri()####
out = ""####
for case in range(cases):####
    n,s = rt()
    n = int(n)
    standing = 0
    extra = 0
    for shyness in range(n+1):
        if int(s[shyness]) == 0:
            continue
        if standing < shyness:
            extra += shyness-standing
            standing += shyness-standing
        standing += int(s[shyness])
    out += "Case #{}: {}\n".format(case+1, extra)####
f.close()####
out = out.strip()####
o = open("a.out", "w")####
o.write(out)####
o.close()####