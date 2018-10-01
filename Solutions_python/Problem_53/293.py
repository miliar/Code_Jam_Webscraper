#!/opt/local/bin/python3.1
import sys

def is_on(length, count):
    return (count + 1) % (2 ** length) == 0

def main(argv=None):
    if len(argv) < 2:
        print('the input file name required')
        sys.exit(1)

    infile = open(argv[1], 'r')
    outfile = open('result.txt', 'w')

    n_testcases = int(infile.readline())
    count = 0
    for line in infile:
        count += 1
        length, times = [int(s) for s in line.split()]
        print('Case #{0}: {1}'.format(count, 'ON' if is_on(length, times) else 'OFF'), file=outfile)


    if not n_testcases == count:
        print('{0} lines left. something wrong with the input file'.format(n_testcases - count))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
