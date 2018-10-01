def isHappy(n, base):
    alreadyVisited = []
    while True:
        res = 0
        while n:
            d = n % base
            res += d * d
            n /= base
        n = res
        if n == 1:
            return True
        elif n in alreadyVisited:
            return False
        else:
            alreadyVisited.append(n)

infile = open("A-small-attempt0.in")
outfile = open("A-small-attempt0.out", "w")
T = int(infile.readline())
for testcaseN in range(T):
    bases = [int(n) for n in infile.readline().split()]
    i = 1
    found = False
    while not found:
        i += 1
        found = True
        for base in bases:
            if not isHappy(i, base):
                found = False
                break
    outfile.write("Case #" + str(testcaseN + 1) + ": " + str(i) + "\n")