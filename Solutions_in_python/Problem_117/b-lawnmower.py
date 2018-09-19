# python 2.7
# Problem B: Lawnmower

def answer(case, s):
    return "Case #%d: %s"%(case, s)

def isMowable(m):
    w = len(m[0])
    # Generate lists of all max-heights per row or column
    rowHeights = [max(row) for row in m]
    colHeights = [max(col) for col in zip(*m)] # my lucky day, twice!
    for y, row in enumerate(m):
        for x in range(w):
            h = row[x]
            if h < rowHeights[y] and h < colHeights[x]: return False
    return True

if __name__ == "__main__":
    def parse_run(s):
        allLines = [map(int, x.split()) for x in s.split("\n") if x]
        count, = allLines[0]

        lines = allLines[1:]
        for i in range(count):
            N, M = lines[0] # no more common (M rows, N columns) syntax ;)
            m = lines[1:1 + N]
            lines = lines[1 + N:]

            print answer(i + 1, "YES" if isMowable(m) else "NO")

    import sys
    try: fn = sys.argv[1]
    except IndexError: fn = "B-large.in"

    with file(fn) as fp:
        parse_run(fp.read())
