from sys import argv, setrecursionlimit
import linecache
import copy

filename = argv[1]
num = int(linecache.getline(filename, 1))

def read(line):
    return map(float, linecache.getline(filename, line).strip().split())

def dw(naomi, ken):
    score = 0

    while(len(naomi) > 0):

        # Cannot win anything with this block.
        if min(naomi) < min(ken):
            n = min(naomi)
            k = max(ken)

        else:
            n = min(naomi)
            k = min(ken)

        naomi.remove(n)
        ken.remove(k)

        if n > k:
            score += 1

    return score

def w(naomi, ken):
    score = 0

    while len(naomi) > 0:
        n = max(naomi)

        if n > max(ken):
            k = min(ken)
        else:
            k = max(ken)
            for alt in ken:
                if alt < k and alt > n:
                    k = alt

        naomi.remove(n)
        ken.remove(k)

        if n > k:
            score += 1

    return score

for i in range(num):
    naomi = read(3*i+3)
    ken = read(3*i+4)

    print "Case #%i: %i %i" % (i+1,
            dw(copy.copy(naomi), copy.copy(ken)),
            w(copy.copy(naomi), copy.copy(ken)))

