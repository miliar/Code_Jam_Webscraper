def method1(items):
    total = 0
    for index in range(0, len(items) - 1):
        diff = items[index] - items[index + 1]
        if diff > 0:
            total += diff
    return total

def getMaxDiff(items):
    maxDiff = 0
    for index in range(1, len(items)):
        diff = items[index - 1] - items[index]
        if diff > 0 and maxDiff < diff:
            maxDiff = diff
    return maxDiff

def method2(items):
    maxDiff = getMaxDiff(items)
    total = 0
    for index in range(0, len(items) - 1):
        item = items[index]
        if item < maxDiff:
            total += item
        else:
            total += maxDiff
    return total

nbCases = int(raw_input())

for nCase in range(nbCases):
    nbItems = int(raw_input())
    items = list(map(int, raw_input().split()))
    total1 = method1(items)
    total2 = method2(items)
    print('Case #' + str(nCase + 1) + ': ' + str(total1) + ' ' + str(total2))
