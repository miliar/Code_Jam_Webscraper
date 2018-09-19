#! /usr/bin/env python


def read_answer(f):
    string_number = int(f.readline())
    result = []
    for i in xrange(4):
        string = f.readline()
        if (i + 1) == string_number:
            result = [int(x.rstrip('\n')) for x in string.split(' ')]

    return result


def get_result(l1, l2):
    result = set()

    for i in l1:
        for j in l2:
            if i == j:
                result.add(i)

    if len(result) > 1:
        return 'Bad magician!'
    if len(result) == 1:
        return result.pop()
    if len(result) == 0:
        return 'Volunteer cheated!'


def print_results(f, results):
    with open(f, 'w') as output:
        for k, v in results.iteritems():
            output.write('Case #{0}: {1}\n'.format(k + 1, v))


def main():
    results = {}

    with open('data/problem_a.input', 'r') as input_file:
        test_cases = int(input_file.readline())
        for i in xrange(test_cases):
            l1 = read_answer(input_file)
            l2 = read_answer(input_file)

            results.setdefault(
                i,
                get_result(l1, l2)
            )

    print_results("data/problem_a.output", results)


if __name__ == '__main__':
    main()
