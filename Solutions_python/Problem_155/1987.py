import sys

def minRequiredForStandingOvation(initialLevels):
    numClapping = initialLevels[0]
    numFriendsRequired = 0

    for i in range(1, len(initialLevels)):
        while numClapping < i:
            numClapping += 1
            numFriendsRequired += 1

        numClapping += initialLevels[i]

    return numFriendsRequired


def main():
    getLine = raw_input
    f = None
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        getLine = f.readline

    numTests = int(getLine())
    for test in range(numTests):
        rawShynessLevels = getLine().split(" ")[1].strip()
        shynessLevels = map(int, rawShynessLevels)

        print("Case #{}: {}".format(test + 1, minRequiredForStandingOvation(shynessLevels)))

    if f:
        f.close()

if __name__ == "__main__":
    main()
