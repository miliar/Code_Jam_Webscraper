def solve(pancakes, k):
    pancakes = list(p == '+' for p in pancakes)
    result = 0
    for i in xrange(len(pancakes) - k + 1):
        if not pancakes[i]:
            for j in xrange(i, i + k):
                pancakes[j] = not pancakes[j]
            result += 1
    return str(result) if all(pancakes) else "IMPOSSIBLE"

if __name__ == '__main__':
    import sys
    fp = open(sys.argv[1])
    def readline():
        return fp.readline().strip()
    num_cases = int(readline())
    for i in xrange(num_cases):
        pancakes, k = readline().split()
        k = int(k)
        print "Case #%d: %s" % (i + 1, solve(pancakes, k))
