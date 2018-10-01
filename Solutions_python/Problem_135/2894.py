import sys
import re


inf = sys.stdin
outf = sys.stdout

m_size = 4


def handle_case(case_num):
    first_answer = int(inf.readline())
    first_matrix = []
    for _ in range(m_size):
        row = map(int, inf.readline().strip().split())
        first_matrix.append(row)
    second_answer = int(inf.readline())
    second_matrix = []
    for _ in range(m_size):
        row = map(int, inf.readline().strip().split())
        second_matrix.append(row)
    first_row = first_matrix[first_answer - 1]
    second_row = second_matrix[second_answer - 1]
    intersection = []
    for i in first_row:
        if i in second_row:
            intersection.append(i)
    if len(intersection) == 1:
        res = str(intersection[0])
    elif len(intersection) > 1:
        res = 'Bad magician!'
    else:
        res = 'Volunteer cheated!'
    case_str = 'Case #{0}: {1}'.format(case_num, res)
    print >>outf, case_str


def main():
    if len(sys.argv) > 1:
        global inf
        inf = open(sys.argv[1])
    if len(sys.argv) > 2:
        global outf
        outf = open(sys.argv[2], 'w')

    T = int(inf.readline().strip())
    for case_num in xrange(1, T+1):
        handle_case(case_num)

    if inf != sys.stdin:
        inf.close()
    if outf != sys.stdout:
        outf.close()


if __name__ == '__main__':
    main()
