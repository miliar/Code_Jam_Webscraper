import sys

infile_path = 'standing_ovation.in'
outfile_path = 'standing_ovation.out'

ROW = 0
COL = 0
MINE_COUNT = 0


def read_data(infile):
    line = infile.readline().strip()
    data_list = line.split()
    data_list_int = []
    for idx in range(len(data_list[1])):
        data_list_int.append(int(data_list[1][idx]))
    return int(data_list[0]), data_list_int


def find_solution(data):
    s_size = data[0]
    s_data = data[1]
    s_need = 0
    s_current = 0
    if s_data[0] == 0:
        s_need = 1
    else:
        s_current = s_data[0] -1
    for idx in range(1, s_size):
        if s_data[idx] == 0:
            if s_current < 1:
                s_need += 1
            else:
                s_current -= 1
        else:
            s_current += s_data[idx] -1
    return s_need


if __name__ == '__main__':
    # opening
    if len(sys.argv) >= 2:
        infile_path = sys.argv[1]
    outfile = None
    if len(sys.argv) >= 3:
        print 'file writing %s' % (sys.argv[2])
        outfile_path = sys.argv[2]
        outfile = open(outfile_path, 'w')
    infile = open(infile_path, 'r')
    outfile = open(outfile_path, 'w')

    # start
    T = int(infile.readline().strip())
    for caseN in xrange(1, T + 1):
        result = find_solution(read_data(infile))
        out_line = 'Case #%i: %s\n' % (caseN, result)

        if outfile is None:
            print out_line
        else:
            outfile.write(out_line)

    # closing
    infile.close()
    if outfile is not None:
        outfile.close()
