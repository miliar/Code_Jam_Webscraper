def isTidy(a):
    current = a[0]
    for i in range(len(a)):
        if a[i] < current:
            return False
        else:
            current = a[i]
    return True


t = int(raw_input())
for i in xrange(1, t + 1):
    n = str(raw_input())
    numList = list(n)

    while not isTidy(numList):
        prev = int(numList[0])
        for j in range(1, len(numList)):
            if int(numList[j]) < prev:
                numList[j-1] = str(int(numList[j-1]) - 1)
                for k in range(j, len(numList)):
                    numList[k] = '9'
                prev = int(numList[0])
                j = 1
            else:
                prev = int(numList[j])

    tidy = ''.join(numList)
    tidy = tidy.lstrip("0")

    print "Case #{}: {}".format(i, tidy)
