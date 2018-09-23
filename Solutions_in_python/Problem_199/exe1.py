

class Panckake:

    def __init__(self, sign):
        self.sign = sign
        self.indexes = []




def readInput(filePath):
    with open(filePath) as f:
        content = f.readlines()

    isFirst = True
    pancakesRows = []
    for line in content:
        if isFirst:
            isFirst = False
            continue

        line = line.rstrip()
        splitted = line.split(' ')
        k = int(splitted[1])


        states = splitted[0].strip()
        pancakes = []
        for state in states:
            if state == '-':
               pancakes.append(Panckake(False))
            elif state =='+':
                pancakes.append(Panckake(True))

        pancakesRows.append([pancakes, k])

    return pancakesRows


def setIndexes(k, pancakes):

    for index, pancake in enumerate(pancakes):

        left = index -  k  +1

        while left <= index:

            if left >= 0:
                right = left + k -1

                if right < len(pancakes):

                    currentIndex= left

                    indexes = []
                    while(currentIndex <= right):
                        indexes.append(currentIndex)
                        currentIndex +=1

                    pancake.indexes.append(indexes)


            left += 1



def clonePancakeArr(pancakes):
    newList = []
    for pancake in pancakes:
        newPancake = Panckake(pancake.sign)
        newPancake.indexes = list(pancake.indexes)
        newList.append(newPancake)

    return newList


def findMin(allPancakes):

    minFound = None
    steps = [[allPancakes,0]]

    while len(steps) > 0:
        added = False
        pancakesStepsPair = steps[0]
        steps.remove(pancakesStepsPair)
        pancakes = pancakesStepsPair[0]
        stepsDone = pancakesStepsPair[1]

        if minFound is not None and stepsDone >= minFound:
                continue

        allPos = True
        for pancake in pancakesStepsPair[0]:
            if pancake.sign == False:
                allPos = False
                if len(pancake.indexes) == 0:
                    break
                else:
                    for indexes in pancake.indexes:
                        cloned = clonePancakeArr(pancakes)
                        for index in indexes:
                            cloned[index].indexes.remove(indexes)
                            if cloned[index].sign:
                                cloned[index].sign = False
                            else:
                                cloned[index].sign = True

                        added = True
                        steps.append([cloned, stepsDone + 1])

                    break

        if allPos:
            if minFound is None or minFound > stepsDone:
                minFound = stepsDone


        if added:
            steps = sorted(steps, key=lambda tup: tup[1])

    return minFound




def paly(k, pancakes):
    setIndexes(k, pancakes)
    res = findMin(pancakes)
    return res






def run():
    rows = readInput('A-small-attempt4.in')
    resRows= []
    index = 1
    for   pankakes,  k in  rows:
        print('index {0}'.format({index}))
        res = paly(k,pankakes)

        if res is not None:
            row = 'Case #{0}: {1}\n'.format(index, res)
        else:
            row = 'Case #{0}: {1}\n'.format(index, 'IMPOSSIBLE')

        resRows.append(row)

        index += 1


    with open('test_exe1out.txt', 'wt') as f:
        for row in resRows:
            f.write(row)





if __name__ == '__main__':
    run()



