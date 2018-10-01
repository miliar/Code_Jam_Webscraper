import fileinput

def main():
    input = []
    for line in fileinput.input():
        input.append(line)

    numcases = int(input[0])

    for i in xrange(numcases):
        row1_id = int(input[10 * i + 1])
        row2_id = int(input[10 * i + 6])
        row1 = [int(num) for num in input[10 * i + 1 + row1_id].split()]
        row2 = [int(num) for num in input[10 * i + 6 + row2_id].split()]
        possibilities = []
        for elem in row1:
            if elem in row2:
                possibilities.append(elem)
        if len(possibilities) == 0:
            print 'Case #' + str(i+1) + ': Volunteer cheated!'
        if len(possibilities) == 1:
            print 'Case #' + str(i+1) + ': ' + str(possibilities[0])
        if len(possibilities) > 1:
            print 'Case #' + str(i+1) + ': Bad magician!'


if __name__ == '__main__':
    main()
