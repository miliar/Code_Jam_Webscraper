
def numOfFlips(stack, k):

    numOfFlipsDone = 0

    for index in range(len(stack) - k + 1):
        if stack[index] == 0:
            numOfFlipsDone += 1

            for index2 in range(index, index + k):
                stack[index2] = (stack[index2] + 1) % 2

    for index in range(len(stack) - k + 1, len(stack)):
        if stack[index] == 0:
            return None

    return numOfFlipsDone


def main():

    numToCheck = []

    for i in range(0, int(raw_input())):

        newList = []

        pancakes, k = raw_input().split(' ')

        for char in pancakes:
            if char == "-":
                newList.insert(0, 0)
            else:
                newList.insert(0, 1)

        numToCheck.append([newList, k])

    count = 0
    for pancakes, k in numToCheck:
        count += 1
        ret = numOfFlips(pancakes, int(k))

        if ret is None:
            ret = 'IMPOSSIBLE'

        print("Case #{0}: {1}".format(count, ret))


if __name__ == "__main__":
    main()