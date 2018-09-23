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

tidyNumbers()
