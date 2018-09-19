#!/home/chenfzh/bin/python


def readfile(filename):
    f = open(filename)
    c = f.readlines()[1:]
    f.close()
    lines = []
    for i in range(0, len(c)):
        if i % 2 != 0:
            lines.append([int(x) - 1 for x in c[i].split()])
    return lines

def calc(s):
    cnt = len(s)
    for i in range(0, cnt):
        if s[i] == i:
            cnt -= 1;
    return cnt

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        exit(0)
    lines = readfile(sys.argv[1])
    for i in range(0, len(lines)):
        print("Case #%d: %.6f" % (i + 1, calc(lines[i])))
    #print("mo(%d, %d)=%d" % (int(sys.argv[1]), int(sys.argv[2]), mo(int(sys.argv[1]), int(sys.argv[2]))))

