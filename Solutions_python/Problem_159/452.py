def first(a):
    res = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            res += a[i]-a[i+1]
    return res

def second(a):
    drops = []
    for i in range(len(a)-1):
        drops.append(a[i]-a[i+1])
    bestDrop = max(drops)
    rate = bestDrop

    res = 0
    for i in range(len(a)-1):
        res += min(a[i], bestDrop)
    return res




for i in range(input()):
    a = input()
    inpt = map(int, raw_input().split())
    print 'Case #' + str(i+1) + ': ' + str(first(inpt)) + ' ' + str(second(inpt))
