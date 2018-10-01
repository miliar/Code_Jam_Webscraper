import sys

def parse():
    NT = int(input())

    testCases = []
    for i in range(1, NT + 1):
        n = int(input())
        testCases.append(n)
    return testCases


def getMaxTidyNumber(n):
    flippedDigits = [int(i) for i in str(n)][::-1]

    for i in range(len(flippedDigits) - 1):
        # print("i={0}, flippedDigits={1}".format(i, flippedDigits))
        if flippedDigits[i] < flippedDigits[i+1]:
            flippedDigits[0:i+1] = [9]*(i+1)
            flippedDigits[i+1] = flippedDigits[i+1] - 1
            # print("InLoop: i={0}, flippedDigits={1}".format(i, flippedDigits))

    digits = "".join(map(str, flippedDigits[::-1]))

    return int(digits)


def main():
    testCases = parse()
    for i, t in enumerate(testCases):
        solution = getMaxTidyNumber(t)
        print("Case #{0}: {1}".format(i+1, solution))

if __name__ == '__main__':
    main()
