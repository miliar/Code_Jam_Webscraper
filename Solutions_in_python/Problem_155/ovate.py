for tc in range(int(input())):
    audience = input().split()
    most = int(audience[0])
    count = [int(x) for x in audience[1]]
    sums = [0]
    for i in count:
        sums.append(sums[-1] + i)
    sums = sums[1:]

    total = 0
    for i, c in enumerate(sums):
        if (i + 1) > (c + total):
            total += (i + 1) - (c + total)

    print("Case #%d: %s" % (tc + 1, total))
