filename = "aLarge.in"
outputFilename = "output.txt"


def is_tidy(n):
    return list(str(n)) == sorted(str(n))


def solve(f):
    n = int(f.readline().strip())

    current = 10
    while True:
        print n
        if is_tidy(n):
            break
        n = n - (n % current) - 1
        current *= 10
    return n


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
