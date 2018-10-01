def main():
    fileName = "A-large.in"
    file = open(fileName)

    # Loop for the number of tests there are.
    for case in range(1, int(file.readline()) + 1):
        # Read in the pancakes and the flipper size.
        tokens = file.readline().split()
        pancakes = list(tokens[0])
        flipSize = int(tokens[1])

        flipCount = 0
        for index in range(0, len(pancakes) - flipSize + 1):
            if pancakes[index] == "-":
                flipCount += 1
                for flipIndex in range(index, index + flipSize):
                    if pancakes[flipIndex] == "-":
                        pancakes[flipIndex] = "+"
                    else:
                        pancakes[flipIndex] = "-"

        for remainingIndex in range(len(pancakes) - flipSize + 1, len(pancakes)):
            if pancakes[remainingIndex] == "-":
                print("Case #" + str(case) + ": IMPOSSIBLE")
                break
        else:
            print("Case #" + str(case) + ": " + str(flipCount))

if __name__ == "__main__":
    main()
