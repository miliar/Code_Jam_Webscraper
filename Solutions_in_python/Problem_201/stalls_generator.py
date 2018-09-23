__author__ = 'whiterock'


with open('stalls_test.txt') as input_file:
    lines = input_file.readlines()
    print "Number of inputs: {}".format(lines[0])
    for i, case in enumerate(lines[1:]):
        stalls, persons = map(int, case.strip().split(' '))
        sequence = [stalls]

        for person in xrange(persons):
            maximum = max(sequence)
            index = sequence.index(maximum)

            if maximum % 2 != 0:
                left = maximum // 2
            else:
                left = maximum // 2 - 1

            right = maximum // 2

            sequence[index] = left
            sequence.insert(index, right)

            if person == persons-1:
                print "Case #{}: {} {}".format(i+1, max(left, right), min(left, right))