import sys


def smallestBiggest(num, listofnums):
    result = None
    for x in listofnums:
        if x > num and ((result is None) or ((x-num) < (result - num))):
            result = x
    if result is None:
        return 1
    return result


if __name__ == '__main__':
    testCasesCount = raw_input()
    for i in range(0, int(testCasesCount)):
        noBlocks = int(raw_input())
        naomiBlocks = map(float, raw_input().split())
        kenBlocks = map(float, raw_input().split())

        sNaomiBlocks = sorted(naomiBlocks)
        sKenBlocks = sorted(kenBlocks)

        naomiPointsDec = 0
        kenIndex = 0
        naomiIndex = 0
        for j in range(0, noBlocks):
            #print naomiPointsDec, sNaomiBlocks[naomiIndex]
            if sNaomiBlocks[naomiIndex] < sKenBlocks[kenIndex]:
                naomiIndex += 1
            else:
                naomiIndex += 1
                naomiPointsDec += 1
                kenIndex += 1

        naomiPointsWar = 0
        for b in naomiBlocks:
            warNextBlockKen = smallestBiggest(b, kenBlocks)
            if warNextBlockKen == 1:
                naomiPointsWar += 1
            else:
                kenBlocks.remove(warNextBlockKen)

        sys.stdout.write("Case #" + str(i + 1) + ": " + str(naomiPointsDec) + " " +str(naomiPointsWar))
        print ""
