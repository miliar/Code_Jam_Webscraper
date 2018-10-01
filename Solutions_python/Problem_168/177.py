
import collections

DIRS = {">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
        "^": (-1, 0)}

def explore(r, c, i, j, maplocs, visited):
    if maplocs[i][j] == "." or (i, j) in visited:
        return 0
    else:
        cnt = 0
        di, dj = DIRS[maplocs[i][j]]
        visited.add((i, j))
        i += di
        j += dj
        while i >= 0 and i <= r -1 and j >= 0 and j <= c - 1:
            if maplocs[i][j] != ".":
                if (i, j) in visited:
                    return 0
                else:
                    return explore(r, c, i, j, maplocs, visited)
            i += di
            j += dj

        if i < 0 or i >= r or j < 0 or j >= c:
            return 1

if __name__ == "__main__":

    T = int(raw_input())
    for mD in xrange(T):
        r, c = map(int, raw_input().split())
        maplocs = []
        for i in xrange(r):
            maplocs.append(raw_input())

        problem = False
        totByRow = collections.Counter()
        totByCol = collections.Counter()
        for i in xrange(r):
            for j in xrange(c):
                if maplocs[i][j] in DIRS:
                    totByRow[i] += 1
                    totByCol[j] += 1
        for i in xrange(r):
            for j in xrange(c):
                if maplocs[i][j] in DIRS and totByRow[i] == 1 and totByCol[j] == 1:
                    problem = True
                    break

        if problem:
            print "Case #%s: %s" % (mD + 1, "IMPOSSIBLE")
        else:
            visited = set()
            numNeeded = 0
            for i in xrange(r):
                for j in xrange(c):
                    numNeeded += explore(r, c, i, j, maplocs, visited)
            print "Case #%s: %s" % (mD + 1, numNeeded)