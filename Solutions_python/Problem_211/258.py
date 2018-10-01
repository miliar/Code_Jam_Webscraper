import math
import functools

#fron itertools library
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def calculateChance(cores, k):
    combs = combinations(cores, k)
    totalchance = 1.0
    for c in combs:
        totalchance *=  1 - functools.reduce(lambda x, y: x * y, c)
    return 1 - totalchance

def findSolution(cores, mustSucceed, bonus):
    remainingBonus = bonus
    coresSorted = sorted(cores)[::-1]
    coresImportant = coresSorted[:mustSucceed][::-1]
    coresUnimportant = coresSorted[mustSucceed:][::-1]
    divideFurther = True
    lastEquals = 1
    while divideFurther:
        lastRound = False
        diff = 0
        nextTarget = 0
        if lastEquals == len(coresImportant):            
            diff = 1 - coresImportant[lastEquals - 1]
            nextTarget = 1
            lastRound = True
        else:
            nextTarget = coresImportant[lastEquals]
            diff = nextTarget - coresImportant[lastEquals - 1]
        totalWant = diff * lastEquals
        if totalWant < remainingBonus:
            for i in range(0, lastEquals):
                coresImportant[i] = nextTarget
            remainingBonus -= totalWant
            lastEquals += 1
        else:
            remainingDivider = remainingBonus / lastEquals
            for i in range(0, lastEquals):
                coresImportant[i] += remainingDivider
            remainingBonus = 0
            divideFurther = False
        if lastRound:
            break
           
    if remainingBonus > 0:
        divideFurther = True
        lastEquals = 1
        while divideFurther:
            lastRound = False
            diff = 0
            nextTarget = 0
            if lastEquals == len(coresUnimportant):            
                diff = 1 - coresUnimportant[lastEquals - 1]
                nextTarget = 1
                lastRound = True
            elif lastEquals > len(coresUnimportant):
                break
            else:
                print(str(lastEquals) + " " + str(len(coresUnimportant)))
                nextTarget = coresUnimportant[lastEquals]
                diff = nextTarget - coresUnimportant[lastEquals - 1]
            totalWant = diff * lastEquals
            if totalWant < remainingBonus:
                for i in range(0, lastEquals):
                    coresUnimportant[i] = nextTarget
                remainingBonus -= totalWant
                lastEquals += 1
            else:
                remainingDivider = remainingBonus / lastEquals
                for i in range(0, lastEquals):
                    coresUnimportant[i] += remainingDivider
                remainingBonus = 0
                divideFurther = False
            if lastRound:
                break
    #print(coresImportant) 
    #print(coresUnimportant) 
    return str(calculateChance(coresImportant + coresUnimportant, mustSucceed))

inp = open("C-small-1-attempt0.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
for i in range(cases):
    total, mustSucceed = list(map(int, inp.readline().rstrip().split(" ")))
    bonus = float(inp.readline().rstrip())
    cores = list(map(float, inp.readline().rstrip().split(" ")))
    res.write("Case #" + str(i+1) + ": " + findSolution(cores, mustSucceed, bonus) + "\n")
    print(i)