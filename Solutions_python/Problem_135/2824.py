import sys
N = 0
L = ""
T = 1
grid = [None] * 4
grid2 = [None] * 4
chosen1 = 0
chosen2 = 0


def getCaseData(fp):
    global L
    L = fp.readline()
    L = int(L.replace("\n", ""))

    global chosen1, chosen2, grid, grid2
    chosen1 = L - 1

    for i in range(0, 4):
        grid[i] = [None] * 4
        grid[i] = map(int, fp.readline().split(" "))

    chosen2 = fp.readline()
    chosen2 = int(chosen2.replace("\n", "")) - 1

    for i in range(0, 4):
        grid2[i] = [None] * 4
        grid2[i] = map(int, fp.readline().split(" "))


def getItems():
    global N, L, T
    global grid, grid2, chosen1, chosen2

    firstOption = grid[chosen1]
    secondOption = grid2[chosen2]


    r = set(firstOption) & set(secondOption)

    if len(r) > 1:
        tstr = "Bad magician!"
    elif len(r) == 0:
        tstr = "Volunteer cheated!"
    else:
        tstr = str(r.pop())

    print "Case #{0}: {1}".format(int(T), tstr)


def main(argv):
    global N, L, T
    infile = argv[0]
    #open file
    fp = open(infile)

    N = fp.readline()
    for i in range(0, int(N)):
        getCaseData(fp)
        getItems()
        T += 1


if __name__ == "__main__":
    main(sys.argv[1:])
