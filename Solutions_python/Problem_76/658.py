score=lambda bag:reduce(int.__xor__, bag, 0)
for testCase in range(1, input() + 1):
    numCandy = input()
    candy = map(int, raw_input().split())

    perm = 1
    res = 0
    while perm < (2**numCandy-1):
        b = bin(perm)[2:]
        b = (numCandy - len(b)) * '0' + b

        sean = []
        pat = []
        for i,d in enumerate(b):
            if d == '1':
                sean.append(candy[i])
            else:
                pat.append(candy[i])

        if score(pat) == score(sean):
            res = max(res, sum(sean))

        perm += 1

    print ("Case #%d: " % (testCase, )) + ("NO" if res == 0 else str(res))
