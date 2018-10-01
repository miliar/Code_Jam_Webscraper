import sys


def read_inputs(filename):
    f = open(filename, 'rt')

    inputs = []

    count = int(f.readline())
    for c in xrange(count):
        sizes = [int(x) for x in f.readline().split(' ')]
        n, m = sizes[0], sizes[1]

        matrix = []
        for lc in xrange(n):
            line = f.readline()
            matrix.append([int(x) for x in line.split(' ')])

        inputs.append((n, m, matrix))

    f.close()

    return inputs

def check_matrix(n, m, matrix):
    for row in xrange(n):
        for col in xrange(m):
            value = matrix[row][col]

            hline = matrix[row][:]
            vline = []
            for k in xrange(n):
                vline.append(matrix[k][col])

            hline.pop(col)
            vline.pop(row)

            h_allowed = len([x for x in hline if x > value])
            v_allowed = len([x for x in vline if x > value])
            if h_allowed > 0 and v_allowed > 0:
                print 'NO'
                return
    print 'YES'


def main():
    inputs = read_inputs(sys.argv[1])

    idx = 1
    for (n, m, matrix) in inputs:
        print 'Case #{}:'.format(idx),
        check_matrix(n, m, matrix)
        idx += 1

if __name__ == '__main__':
    main()
