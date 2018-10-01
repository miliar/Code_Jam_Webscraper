import sys

def process(row1, row2):

    num = list(set(row1).intersection(set(row2)))

    total = len(num)

    if total == 1:
        return num[0]
    elif total > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


if __name__ == "__main__":

    f = sys.stdin

    if len(sys.argv) >= 2:

        fn = sys.argv[1]

        if fn != '-':
            f = open(fn)

    total = int(f.readline())

    for i in xrange(total):

        r1 = int(f.readline())
        row1 = []

        for r in xrange(1, 5):
            inum = f.readline()
            if r == r1:
                row1 = ([int(j) for j in inum.split()])

        r2 = int(f.readline())
        row2 = []

        for r in xrange(1, 5):
            inum = f.readline()
            if r == r2:
                row2 = ([int(j) for j in inum.split()])

        print "Case #%d: %s" % (i + 1, process(row1, row2))
