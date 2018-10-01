import sys
from common import parse_input

def get_matrix(f):
    matrix = []
    for i in range(4):
        matrix.append(map(lambda ip: int(ip), f.readline().rstrip().split(' ')))
    return matrix

if __name__ == '__main__':
    op = open("op", "w")
    sys.stdout = op
    t, f = parse_input('A-small-attempt0.in')
    for tc in range(t):
        pos1 = int(f.readline())
        matrix1 = get_matrix(f)
        pos2 = int(f.readline())
        matrix2 = get_matrix(f)
        intersection = list(set(matrix1[pos1 - 1]).intersection(set(matrix2[pos2 - 1])))
        op = None
        if intersection:
            if len(intersection) > 1:
                op = 'Bad magician!'
            else:
                op = intersection[0]
        else:
            op = 'Volunteer cheated!'
        print 'Case #%d: %s' % (tc + 1, op)
    f.close()
    op.close()

