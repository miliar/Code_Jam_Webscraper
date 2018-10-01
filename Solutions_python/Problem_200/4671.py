

def readInput(filePath):
    with open(filePath) as f:
        content = f.readlines()

    numbers = []
    isFirst = True
    pancakesRows = []
    for line in content:
        if isFirst:
            isFirst = False
            continue

        numbers.append(line.strip())

    return numbers





def maxForNum(num):
    digits = []
    index = len(num) -1
    while index >= 0:
        dig = int(num[index])
        digits.insert(0, dig)
        #current = int(current / 10)
        index = index -1

    if len(digits) == 1:
        return digits[0]

    lastIndex = len(digits) -1
    firstChange = True
    while lastIndex > 0:
        if digits[lastIndex] < digits[lastIndex-1]:

            if lastIndex < len(digits) -1 and firstChange:
                fromIndex = lastIndex + 1

                while fromIndex < len(digits):
                    digits[fromIndex] = 9
                    fromIndex += 1

            digits[lastIndex] = 9

            firstChange = False

            if lastIndex -1 == 0 and  digits[lastIndex-1] - 1 == 0:
                newDigits = []
                indexStart = 0
                while indexStart < len(digits) -1:
                    newDigits.append(9)
                    indexStart  += 1

                digits = newDigits
                break
            else:
                digits[lastIndex-1] = digits[lastIndex-1] - 1

            # if lastIndex < len(digits) -1:
            #     if lastchanedIndex != lastIndex + 1:
            #         lastIndex = lastIndex + 1
            #         continue

            lastchanedIndex = lastIndex

        lastIndex -= 1

    num = digits[0]
    for digit in digits[1:]:
        num = num * 10 + digit

    return num


def run():
    numbers = readInput('B-small-attempt1.in')

    index = 1
    with open('test_exe2out.txt', 'wt') as f:
        for num in numbers:
            maxFounnd = maxForNum(num)
            f.write('Case #{0}: {1}\n'.format(index, maxFounnd))
            index += 1









if __name__ == '__main__':
    run()