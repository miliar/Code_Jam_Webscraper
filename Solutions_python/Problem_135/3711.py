
def readFile(filename):
    f = open(filename, 'r')
    totalCases = int(f.readline()[:-1])
    cases = []
    for _ in range(totalCases):
        case = []
        for _ in range(10):
            line = f.readline()
            if '\n' in line:
                line = line[:-1]
            case.append(map(int, line.split(' ')))
        cases.append(case)
    f.close()
    return cases

def performMagicTrick(infile, outfile):
    cases = readFile(infile)
    output = []
    for index, case in enumerate(cases):
        index1 = case[0][0]
        index2 = case[5][0]
        n1 = case[index1]
        n2 = case[index2 + 5]
        numbers = list(set(n1) & set(n2))
        if len(numbers) == 0:
            output.append('Case #' + str(index + 1) + ": Volunteer cheated!")
        elif len(numbers) == 1:
            output.append('Case #' + str(index + 1) + ": " + str(numbers[0]))
        else:
            output.append('Case #' + str(index + 1) + ": Bad magician!")
    output = '\n'.join(output)
    f = open(outfile, 'w')
    f.write(output)
    f.close()




#infile = 'io\A-small-test.in'
infile = 'io\A-small-attempt0.in'
outfile = 'io\A-small-test.out'
performMagicTrick(infile, outfile)