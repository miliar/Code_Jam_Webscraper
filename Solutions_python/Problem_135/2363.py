import sys

def main():
    with open(sys.argv[1]) as inputFile:
        outputFile = open('trick_output.txt', 'w')

        numberCases = int(inputFile.readline())
        for x in range(0, numberCases):
            first_row = int(inputFile.readline()) - 1
            first_config = read_card_config(inputFile)
            second_row = int(inputFile.readline()) - 1
            second_config = read_card_config(inputFile)

            trick_result = set(first_config[first_row]).intersection(set(second_config[second_row]))
            len_result = len(trick_result)
            outputFile.write('Case #' + str(x + 1) + ': ')
            if len_result == 1:
                outputFile.write(str(trick_result.pop()))
            elif len_result == 0:
                outputFile.write('Volunteer cheated!')
            else:
                outputFile.write('Bad magician!')
            outputFile.write('\n')

        outputFile.close()


def read_card_config(inputFile):
    card_config = [[] for i in range(4)]

    for i in range(0, 4):
        line = inputFile.readline().split()
        for token in line:
            card_config[i].extend([int(token)])

    return card_config


if __name__ == "__main__":
    main()