__author__ = 'Arvind Chembarpu'
__email__ = 'achembarpu@gmail.com'


def get_input():
    with open('input.txt', 'r') as in_file:
        for line in in_file.readlines():
            yield line


def comprehend_magic():
    in_data = get_input()
    cases = int(in_data.next())

    chosen_row = [[] for i in xrange(cases)]
    arrangement = [[] for i in xrange(cases)]

    for i in xrange(cases):
        chosen_row[i] = [0 for _ in xrange(2)]
        arrangement[i] = [[] for _ in xrange(2)]
        for j in xrange(2):
            chosen_row[i][j] = int(in_data.next())
            arrangement[i][j] = [in_data.next().split(' ') for _ in xrange(4)]
            for k in xrange(4):
                arrangement[i][j][k] = [int(arrangement[i][j][k][l]) for l in xrange(4)]
        print 'Case #%d: %s' % (i + 1, do_magic(chosen_row[i], arrangement[i]))


def do_magic(row, arr):
    possibles = [[] for _ in xrange(2)]
    for i in xrange(2):
        possibles[i] = arr[i][row[i] - 1]

    matches = []
    for j in xrange(4):
        card = possibles[1][j]
        if card in possibles[0]:
            matches.append(card)

    if len(matches) == 0:
        return 'Volunteer cheated!'
    elif len(matches) == 1:
        return str(matches[0])
    else:
        return 'Bad magician!'


def main():
    comprehend_magic()


if __name__ == '__main__':
    main()