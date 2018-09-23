import copy

def run(file):
    with open(file) as f, open('output.txt', 'w') as ff:
        header = f.readline().strip()
        content = f.readlines()
        content = [x.strip() for x in content]
        row = 1

        for c in content:
            ff.write('Case #' + str(row) + ': ' + str(count(c))+'\n')
            row += 1


def count(line):
    number = int(line)
    numbers = list(line)
    length = len(line)

    if length == 1:
        return number

    copied = copy.copy(numbers)
    copied.sort()
    if copied == numbers:
        return number

    num = '9' * (length - 1)

    for i in range(int(num)):
        subtracted = number - i
        subtractedList = list(str(subtracted))
        sortedList = copy.copy(subtractedList)
        sortedList.sort()
        if sortedList == subtractedList:
            return subtracted

    return '9' * (length - 1)


run('B-small-attempt1.in')