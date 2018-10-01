

inputFile = open('D-large.in', 'rb')

outputFile = open('D-large.out', 'w')

T = int(inputFile.readline().rstrip("\n"))

for t in range(0, T):

    num_blocks = int(inputFile.readline().rstrip("\n"))

    naomi_blocks = inputFile.readline().rstrip("\n").split(" ")
    ken_blocks = inputFile.readline().rstrip("\n").split(" ")

    naomi_blocks = [float(i) for i in naomi_blocks]
    ken_blocks = [float(i) for i in ken_blocks]

    naomi_blocks = sorted(naomi_blocks)
    ken_blocks = sorted(ken_blocks)

    naomi_blocks_dup = naomi_blocks[:]
    ken_blocks_dup = ken_blocks[:]

    # outputFile.write(str(naomi_blocks) + "\n")
    # outputFile.write(str(ken_blocks) + "\n")

    # first get the output if they play properly
    naomi_wins = 0

    for naomi_block in naomi_blocks_dup:
        # get the next largest for ken
        i = 0

        while i < len(ken_blocks_dup) and ken_blocks_dup[i] < naomi_block:
            i += 1

        if i != len(ken_blocks_dup):
            # ken chooses the next largest
            ken_block = ken_blocks_dup[i]
        else: # if not, he chooses the smallest
            ken_block = ken_blocks_dup[0]

        # remove the block he played
        ken_blocks_dup.remove(ken_block)

        # see who won
        if naomi_block > ken_block:
            naomi_wins += 1

    # deceitful
    changed = True
    while changed:
        changed = False
        # print("naomi_blocks", naomi_blocks)
        # print("ken_blocks", ken_blocks)
        if len(naomi_blocks) == 0:
            break
        if naomi_blocks[0] < ken_blocks[0]:
            naomi_blocks.pop(0)
            ken_blocks.pop()
            changed = True

    naomi_wins2 = 0

    while len(naomi_blocks) > 0:
        if naomi_blocks[0] < ken_blocks[0]:
            naomi_blocks.pop(0)
            ken_blocks.pop()
        else:
            naomi_blocks.pop(0)
            ken_blocks.pop(0)
            naomi_wins2 += 1

    # outputFile.write(str(naomi_blocks) + "\n")
    # outputFile.write(str(ken_blocks) + "\n")


    outputFile.write("Case #%d: %d %d\n" % (t+1, naomi_wins2, naomi_wins))

inputFile.close()
outputFile.close()