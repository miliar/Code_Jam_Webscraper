import sys

def numberOfCommon(rowA, rowB):
    count = 0
    for item in rowA:
        if item in rowB:
            count += 1

    return count


def getCommon(rowA, rowB):
    for item in rowA:
        if item in rowB:
            return item


def questionA(answerA, answerB, arrangementA, arrangementB):
    answerA-=1
    answerB-=1

    answerRowA = arrangementA[answerA]
    answerRowB = arrangementB[answerB]

    count = numberOfCommon(answerRowA, answerRowB)
    if count == 0:
        return - 2
    elif count == 1:
        return getCommon(answerRowA, answerRowB)
    else:
        return -1

if __name__ == '__main__':
    filename = sys.argv[1]
    text = open(filename, "r").readlines()
    testcases = int(text[0])
    text = text[1:]

    for index, line in enumerate(text):
        text[index] = line.replace('\n', '')

    outfile = open("out.txt", "a")
    for i in range(testcases):
        answerA = int(text[0])
        arrangementA = [text[1].split(' '),
                        text[2].split(' '),
                        text[3].split(' '),
                        text[4].split(' ')]
        answerB = int(text[5])
        arrangementB = [text[6].split(' '),
                        text[7].split(' '),
                        text[8].split(' '),
                        text[9].split(' ')]

        text = text[10:]
        answer = questionA(answerA, answerB, arrangementA, arrangementB)

        result = "Case #%d: " % (int(i) + 1)
        if answer > 0:
            result += str(answer)
        elif answer == -1:
            result += "Bad magician!"
        elif answer == -2:
            result += "Volunteer cheated!"

        outfile.write(result + "\n")