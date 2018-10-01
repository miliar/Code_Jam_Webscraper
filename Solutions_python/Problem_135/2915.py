def read_ints(file):
    line = file.readline().strip().split()
    result = tuple(map(int, line))
    if len(result) == 1:
        result = result[0]
    return result


def input():
    filename = __file__.split('.')[0] + '.in'
    with open(filename) as file:
        tests_count = int(file.readline().strip())

        for test_index in xrange(tests_count):
            first_answer = int(file.readline().strip())
            first_layout = [read_ints(file) for i in xrange(4)]
            second_answer = int(file.readline().strip())
            second_layout = [read_ints(file) for i in xrange(4)]
            yield first_answer, first_layout, second_answer, second_layout


def output():
    filename = __file__.split('.')[0] + '.out'
    with open(filename, 'w') as file:
        i = 0
        while True:
            value = (yield)
            i += 1
            file.write('Case #%d: %s\n' % (i, value))


def main():
    results = output()
    results.next()

    for task in input():
        first_answer, first_layout, second_answer, second_layout = task

        first_set = set(first_layout[first_answer - 1])
        second_set = set(second_layout[second_answer - 1])

        answers = first_set & second_set

        if len(answers) > 1:
            results.send('Bad magician!')
        elif len(answers) == 1:
            results.send(answers.pop())
        else:
            results.send('Volunteer cheated!')

    results.close()

if __name__ == '__main__':
    main()
