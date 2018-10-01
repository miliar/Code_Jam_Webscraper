
def fixup(numAsStr, pos):

    if (0 == pos) and ('1' == numAsStr[pos]):
        return '9' * (len(numAsStr) - 1)

    return numAsStr[0:pos] + chr(ord(numAsStr[pos]) - 1) + '9' * (len(numAsStr) - pos - 1)

def solve(numAsStr):

    fixPos = 0

    for i in range(1, len(numAsStr)):
        if ord(numAsStr[fixPos]) < ord(numAsStr[i]):
            fixPos = i

        if ord(numAsStr[fixPos]) > ord(numAsStr[i]):
            return fixup(numAsStr, fixPos)

    return numAsStr


def main():

    numToCheck = []

    for i in range(0, int(raw_input())):

        newList = []

        numToCheck.append(raw_input())

    count = 0
    for num in numToCheck:
        count += 1
        ret = solve(num)

        print("Case #{0}: {1}".format(count, ret))


if __name__ == "__main__":
    main()