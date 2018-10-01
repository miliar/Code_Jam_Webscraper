import sys

def main():
    fin = open(sys.argv[1])
    T = int(fin.readline())
    for test in range(1, T + 1):
        # print test
        lines = []
        for l in range(10):
            lines.append(fin.readline())

        r1 = int(lines[0])
        r2 = int(lines[5])

        r1 = map(int, lines[r1].split())
        r2 = map(int, lines[5 + r2].split())

        common = set(r1) & set(r2)
        if not common:
            print "Case #%d: Volunteer cheated!" % test
        elif len(common) != 1:
            print "Case #%d: Bad magician!" % test
        else:
            print "Case #%d: %d" % (test, common.pop())


if __name__ == "__main__":
    main()
