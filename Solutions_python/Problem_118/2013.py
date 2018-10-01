import sys, string, math

def fairsquare(n, m):
    nfair = 0
    ns = int(math.floor(math.sqrt(n)))
    ms = int(math.ceil(math.sqrt(m)))
#    print ns, ms
    for i in range(ns, ms+1):
        s = "%d" % i
        r = s[::-1]
        if s == r:
            square = i*i
            if square < n or square > m: continue
            s = "%d" % square
            r = s[::-1]
            if s == r: nfair += 1
    return nfair

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline().rstrip()
        parts = line.split()
        nums = map(int, parts)
        n, m = nums
        ans = fairsquare(n, m)
        sys.stdout.write("Case #%d: %d\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)
