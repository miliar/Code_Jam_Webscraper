import sys

def parseLine(line):
    start, end, num = [int(elem) for elem in line.split()]
    return (start, end, num)

def getSum(n):
    return (n * (n + 1)) / 2

def getCost(elem, n):
    start, end, num = elem
    A = getSum(n)
    B = getSum(n - (end - start))
    return num * (A - B)

def solve(test):
    n, m = [int(elem) for elem in sys.stdin.readline().split()]
    vec = []
    for i in range(m):
        vec.append(parseLine(sys.stdin.readline()))

    initial = 0
    for v in vec:
        initial += getCost(v, n)

    res = 0
    points = set()
    starting = dict()
    ending = dict()

    for v in vec:
        start, end, num = v
        points.add(start)
        points.add(end)
        addToDict(starting, start, num)
        addToDict(ending, end, num)

    points = list(points)
    points.sort()

    arr = []
    for p in points:
        if starting.has_key(p):
            arr.append((p, starting[p]))

        num = ending.get(p, 0)
        while num > 0:
            k = min(num, arr[-1][1])
            res += getCost((arr[-1][0], p, k), n)
            num -= k
            if arr[-1][1] == k:
                arr.pop()
            else:
                arr[-1] = (arr[-1][0], arr[-1][1] - k)

    print 'Case #{0}: {1}'.format(test, initial - res)


def addToDict(d, key, val):
    new_val = d.get(key, 0) + val
    d[key] = new_val

def main():
    T = int(sys.stdin.readline().strip())
    for test in range(1, T + 1):
        solve(test)

main()
