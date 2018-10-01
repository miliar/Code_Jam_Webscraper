import sys
import copy

infile_path = sys.argv[0].replace('.py', '') + '.in'
outfile_path = sys.argv[0].replace('.py', '') + '.out'


def read_data(infile):
    line = infile.readline().strip()
    data_size = int(line)
    line = infile.readline().strip()
    data_list = line.split()
    data_list_int = []
    for idx in data_list:
        data_list_int.append(int(idx))
    return data_size, data_list_int


def find_two_number(num):
    small = num / 2
    big = num / 2 + num % 2
    numbers = []
    numbers.append([small, big])
    if num % 2 == 1:
        for idx in range(1, small):
            if (num - (small - idx)) == (small - idx) * 2:
                small = small - idx
                big = num - small
                numbers.append([small, big])
                break

    return numbers


def find_minute(min_minute, special, sorted_data):
    print sorted_data
    if special >= min_minute:
        return min_minute

    bignum_count = sorted_data.count(sorted_data[0])
    special += bignum_count
    for small, big in find_two_number(sorted_data[0]):
        print '   ', small, big
        tmp = copy.deepcopy(sorted_data)
        for idx in range(bignum_count):
            tmp[idx] = big
            tmp.append(small)
        tmp.sort(reverse=True)
        if min_minute > special + tmp[0]:
            min_minute = special + tmp[0]
        minute = find_minute(min_minute, special, tmp)
        if min_minute > minute:
            min_minute = minute
    
    return min_minute

def find_solution(data):
    d_size = data[0]
    d_data = data[1]

    d_data.sort(reverse=True)
    min_minute = d_data[0]
    special = 0

    result = find_minute(min_minute, 0, d_data)
    return result


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

        print out_line
        if outfile is None:
            print out_line
        else:
            outfile.write(out_line)

    # closing
    infile.close()
    if outfile is not None:
        outfile.close()
