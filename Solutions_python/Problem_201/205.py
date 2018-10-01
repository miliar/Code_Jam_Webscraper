



t = int(input())

for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]

    depth = k.bit_length() - 1

    pair  = (n, n+1)
    count = [1, 0  ]

    for d in range(0, depth):
        if pair[0]%2 == 0:
            count[1] += 2**d
        else:
            count[0] += 2**d
        p0 = (pair[0]-1)//2
        pair = (p0, p0+1)

    spaces = pair[1]

    if k%(2**depth) >= count[1]:
        spaces = pair[0]

    minS = (spaces - 1) // 2
    maxS = spaces // 2

    print("Case #{}: {} {}".format(i, maxS, minS))
    # check format
