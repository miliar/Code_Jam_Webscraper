filename = "a.in"
# filename = "aLarge.in"
outputFilename = "output.txt"


def solve(f):
    n, r, ry, y, yb, b, br = map(int, f.readline().strip().split(" "))
    N, R, O, Y, G, B, V = n, r, ry, y, yb, b, br

    if ((ry > b or (ry > 0 and ry == b and n > ry + b)) or
        (yb > r or (yb > 0 and yb == r and n > yb + r)) or
        (br > y or (br > 0 and br == y and n > br + y)) or
            (r > b + y) or
            (b > r + y) or
            (y > b + r)):
        return "IMPOSSIBLE"
    arr = ""
    if ry > 0:
        while ry > 0:
            arr += "BO"
            ry -= 1
            b -= 1
            n -= 2
        if b > 0:
            arr += "B"
            b -= 1
            n -= 1

    if yb > 0:
        while yb > 0:
            arr += "RG"
            yb -= 1
            r -= 1
            n -= 2
        if r > 0:
            arr += "R"
            r -= 1
            n -= 1

    if br > 0:
        while br > 0:
            arr += "YV"
            br -= 1
            y -= 1
            n -= 2
        if y > 0:
            arr += "Y"
            y -= 1
            n -= 1

    while n > 0:
        colors = sorted([(r, "R"), (y, "Y"), (b, "B")], reverse=True)
        while colors[-1][0] == 0:
            colors = colors[:-1]
        i = 0

        if arr:
            match = True
            for j in range(len(colors) - 1):
                if colors[j][0] != colors[j + 1][0]:
                    match = False
                    break
            if match:
                # print "MATCH!!!"
                for j in range(len(colors)):
                    if colors[j][1] == arr[0] and colors[j][1] != arr[-1]:
                        i = j
                        break



        # print colors
        # if colors[i][0] == 0:
        #     print colors, i, arr
        #     colors = colors[:i] + colors[i+1:]
        #     i %= len(colors)
        #     print colors, i, arr
        if arr and colors[i][1] == arr[-1]:
            i += 1
        arr += colors[i][1]
        c = colors[i][1]
        if c == "R":
            r -= 1
        elif c == "Y":
            y -= 1
        else:
            b -= 1
        n -= 1

    assert arr[0] != arr[-1], "arr[0] = {}, array = {}".format(arr[0], arr)
    for i in range(N-1):
        assert arr[i] != arr[i-1], "i = {}, arr[i] = {}, array = {}".format(i, arr[i], arr)
    assert arr.count("R") == R, "R = {}, count = {}, array: {}".format(R, arr.count("R"), arr)
    assert arr.count("B") == B, arr
    assert arr.count("Y") == Y, arr
    assert arr.count("O") == O, arr
    assert arr.count("V") == V, arr
    assert arr.count("G") == G, arr
    assert len(arr) == N, arr
    return arr




def out(s, o):
    print s
    o.write("{}\n".format(s))


def main():
    f = open(filename)
    o = open(outputFilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1


if __name__ == "__main__":
    main()
