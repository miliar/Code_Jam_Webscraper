#!/home/chenfzh/bin/python


def calc(com, opp, str):
    res = []
    c = com[0:2]
    for i in str:
        if len(res):
            if i + res[-1] == c or res[-1] + i == c:
                res[-1] = com[-1]
            elif (opp.find(i) == 0 and res.count(opp[1]) > 0) or\
                 (opp.find(i) == 1 and res.count(opp[0]) > 0):
                res = []
            else:
                res.append(i)
        else:
            res.append(i)
    return res

def output(res):
    if len(res) == 0:
        return "[]"
    str = "["
    for i in res:
        str += i + ", "
    str = str[:-2] + "]"
    return str

def readfile(filename, lines):
    f = open(filename)
    c = f.readlines()[1:]
    f.close()
    for i in c:
        t = i.split()
        if t[0] == '0':
            t.insert(1, "")
        if t[2] == '0':
            t.insert(3, "")
        lines.append((t[1], t[3], t[5]))

if __name__ == '__main__':
    import sys
    if len(sys.argv) <=1:
        exit(0)
    lines = []
    readfile(sys.argv[1], lines)
    for i in range(0, len(lines)):
        print("Case #%d: %s" % (i + 1, output(calc(lines[i][0], lines[i][1], lines[i][2]))))
