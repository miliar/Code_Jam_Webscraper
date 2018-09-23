def myMax(l, func= lambda x: x):
    iterator = iter(l)
    currMax = next(iterator)
    while True:
        try:
            nxt = next(iterator)
            if func(currMax) < func(nxt):
                currMax = nxt
        except StopIteration:
            break

    return filter(lambda x: func(x) == func(currMax), l)

def myMin(l, func = lambda x: x):
    iterator = iter(l)
    currMax = next(iterator)
    while True:
        try:
            nxt = next(iterator)
            if func(currMax) > func(nxt):
                currMax = nxt
        except StopIteration:
            break

    return filter(lambda x: func(x) == func(currMax), l)

def pickStall(stalls):
    stallInfo = [(i, getSides(stalls, i)) for i in range(len(stalls))]
    mins = list(myMax(stallInfo, lambda x: min(*x[1])))
    if len(mins) == 1:
        return mins[0]
    else:
        maxs = list(myMax(mins, lambda x: max(*x[1])))
        return maxs[0]


def getSides(stalls, idx):
    if stalls[idx]:
        return (0, 0)
    currIdx = idx - 1
    currCount = 0
    while not stalls[currIdx]:
        currCount += 1
        currIdx -= 1
    left = currCount

    currIdx = idx + 1
    currCount = 0
    while not stalls[currIdx]:
        currCount += 1
        currIdx += 1
    right = currCount

    return (left, right)

def getOutput(n, k):
    stalls = [False] * (n + 2)
    stalls[0] = True
    stalls[-1] = True
    for i in range(k):
        pick = pickStall(stalls)
        stalls[pick[0]] = True
        lastMax = max(pick[1])
        lastMin = min(pick[1])

    return "Case #{}: {} {}".format("{}", lastMax, lastMin)

input()
counter = 0
while True:
    counter += 1
    try:
        n, k = map(int, input().split(" "))
        print(getOutput(n, k).format(counter))
    except (EOFError, ValueError):
        break
