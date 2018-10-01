



t = int(input())

for i in range(1, t + 1):
    # read input
    r, c = [int(s) for s in input().split(" ")]

    cake = [["" for rcake in range(c)] for ccake in range(r)]

    blocks = []
    blockchars = [[] for ri in range(r)]

    for ri in range(0, r):
        blockLine = False

        line = input()
        for ci, ch in enumerate(line):
            cake[ri][ci] = c
            if ch is not "?":
                blockchars[ri].append((ch, ci))

                if not blockLine:
                    blockLine = True
                    blocks.append(ri)

    # print(c, blocks, blockchars)

    for bi, b in enumerate(blocks):
        # [(0, 0), (1, 2)]

        # print(b)

        for bci, bc in enumerate(blockchars[b]):
            # [(0, ('J', 1)), (1, ('A', 2)), (2, ('M', 3))]

            # print(bc)
            isIn = bi+1 < len(blocks)

            startrow = b if bi is not 0 else 0
            endrow = (blocks[bi+1]-1) if isIn else (r-1)
            startcol = bc[1] if bci is not 0 else 0
            endcol = blockchars[bci+1][1]-1 if (bci+1) in blockchars else c-1

            # print(startrow, endrow, startcol, endcol, bc)

            for ni in range(startrow, endrow+1):
                for nj in range(startcol, endcol+1):
                    cake[ni][nj] = bc[0]

    output = "\n".join(["".join(line) for line in cake])

    print("Case #{}:\n{}".format(i, output))
    # check format
