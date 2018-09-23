from sets import Set


def pancakes():
    f = open("input.txt", "r")
    text = f.readlines()

    for i in xrange(1, len(text)):
        test = text[i].strip().split(' ')
        result = flips(test[0], int(test[1]), Set())
        if result == 99999999:
            result = 'IMPOSSIBLE'
        print "Case #" + str(i) + ":" + " " + str(result)


def flips(pancakes, k, states):
    if len(pancakes) == 0:
        return 0

    stack = Set([pancakes])
    flips = 0
    newStack = Set()

    while len(stack) > 0:
        cur = stack.pop()
        s = Set(cur)
        if len(s) == 1 and s.pop() == '+':
            return flips
        if cur in states:
            if len(stack) == 0:
                stack = newStack
                newStack = Set()
                flips += 1
            continue
        states.add(cur)
        for i in range(0, len(cur)-k+1):
            new_cur = cur[0:i] + reverse(cur[i:i+k]) + cur[i+k:]
            #print "new cur", i, new_cur
            newStack.add(new_cur)
        if len(stack) == 0:
            stack = newStack
            newStack = Set()
            flips += 1
            #print "NEW LEVEL", flips, stack

    return 99999999


def reverse(s):
    result = ""
    for c in s:
        if c == "+":
            result += "-"
        elif c == "-":
            result += "+"
    return result

# pancakes()


def tidyNumbers():
    f = open("input.txt", "r")
    text = f.readlines()

    for i in xrange(1, len(text)):
        n = text[i].strip()
        result = lastTidy(n)
        print "Case #" + str(i) + ":" + " " + str(result)


def lastTidy(n):
    if isTidy(n):
        return n

    if len(n) == 1:
        return True

    nInt = int(n)

    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            # chop off!
            maybeTidy = nInt - int(n[i:]) - 1
            s = str(maybeTidy)
            if not isTidy(s):
                return lastTidy(s)
            else:
                return maybeTidy


def isTidy(n):
    if len(n) == 1:
        return True
    for i in range(1, len(n)):
        if n[i-1] > n[i]:
            return False
    return True

#tidyNumbers()

def bathroomStalls():
    f = open("input.txt", "r")
    text = f.readlines()

    for i in xrange(1, len(text)):
        test = text[i].strip().split(' ')
        nStalls = int(test[0])
        k = int(test[1])
        result = lastStall(nStalls, k, ['.' for x in range(int(test[0]))])
        print "Case #{}: {} {}".format(i, result[0], result[1])


def lastStall(n, k, stalls):
    while k > 0:
        #print "k", k
        # number of empty stalls b/w s and closest neighbor
        l_s = [None for x in stalls]
        r_s = [None for x in stalls]
        # for each empty stall, compute Ls and Rs
        lastTaken = -1
        for i, v in enumerate(stalls):
            # stall is empty
            #print "last taken", lastTaken, i, v
            if v == '.':
                if i == 0:
                    l_s[i] = 0
                else:
                    l_s[i] = i-lastTaken-1
            else:
                lastTaken = i

        lastTaken = len(stalls)
        for i in range(len(stalls)-1, -1, -1):
            # stall is empty
            if stalls[i] == '.':
                r_s[i] = lastTaken-i-1
            else:
                lastTaken = i

        #print "l_s", l_s
        #print "r_s", r_s
        maxOfMinStalls, maxOfMin = getMaxOfMin(l_s, r_s)
        stallChoice, maxOfMax = getMaxOfMax(l_s, r_s, maxOfMinStalls)

        stalls[stallChoice] = 'O'
        #print "stalls", stalls
        k -= 1

    return (maxOfMax, maxOfMin)


def getMaxOfMin(l_s, r_s):
    minLsRs = [None for x in l_s]

    curMax = -1
    stallN = []

    for i in range(len(l_s)):
        if l_s[i] is None:
            continue
        minLsRs = min(l_s[i], r_s[i])
        #print curMax, minLsRs
        if minLsRs > curMax:
            stallN = [i]
            curMax = minLsRs
        elif minLsRs == curMax:
            stallN.append(i)
    #print "max of min", stallN, curMax
    return (stallN, curMax)


def getMaxOfMax(l_s, r_s, stalls):
    curMax = []
    stallN = []

    curMax = -1

    for i in stalls:
        maxLsRs = max(l_s[i], r_s[i])
        if maxLsRs > curMax:
            stallN = [i]
            curMax = maxLsRs
        elif maxLsRs == curMax:
            stallN.append(i)
    #print "max of max", stallN, curMax
    return (stallN[0], curMax)

bathroomStalls()

# lastStall(5, 0, [None for i in range(5)])
