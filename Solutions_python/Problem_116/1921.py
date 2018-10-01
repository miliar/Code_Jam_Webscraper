import sys
import itertools

def process_file(path):
    with open(path, 'r') as file_handle:
        case_count = int(file_handle.readline().strip())
        test_case_list = []
        for i in xrange(case_count):
            test_case = [file_handle.readline().strip() for i in xrange(4)]
            test_case_list.append(test_case)
            file_handle.readline()

        return test_case_list

def process_row(row):
    if row[0] in ('T', 'O', 'X'):
        if set(row) in ({'X'}, {'X', 'T'}):
            return 'X won'
        elif set(row) in ({'O'}, {'O','T'}):
            return 'O won'

def get_diagonals(test_case):
    l = len(test_case)
    return ([test_case[i][i] for i in xrange(l)],
            [test_case[l-1-i][i] for i in xrange(l-1,-1,-1)]
            )

def process_test_case(test_case):
    for row in test_case:
        result = process_row(row)
        if result is not None:
            return result

    for row in zip(*test_case):
        result = process_row(row)
        if result is not None:
            return result

    for row in get_diagonals(test_case):
        result = process_row(row)
        if result is not None:
            return result


    if '.' in itertools.chain.from_iterable(test_case):
        return 'Game has not completed'

    return 'Draw'

if __name__ == '__main__':
    test_case_list = process_file(sys.argv[1])
    for i, test_case in enumerate(test_case_list):
        print 'Case #{}:'.format(i+1), process_test_case(test_case)
