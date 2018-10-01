import sys
import time
import msvcrt
import logging
from multiprocessing import Pool

ACTIVE_PROCESSES = 8


def test_one_case(arg):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    result = 0
    case, a, b, k = arg

    catalina = range(k)

    for a_value in xrange(a):
        for b_value in xrange(b):
            if (a_value & b_value) in catalina:
                result += 1

    return case, result


def main():
    with open(sys.argv[1], 'rb') as fh:
        inp = fh.readlines()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    t = int(inp.pop(0))
    results_file = sys.argv[1] + '.out'

    pool = Pool(ACTIVE_PROCESSES)

    data = list()
    for i in range(t):
        a, b, k = map(int, inp.pop(0).strip().split())
        data.append([i, a, b, k])

    cases = pool.map(test_one_case, data)

    with open(results_file, 'wb') as fh:
        for case, wins in cases:
            line = "Case #%d: %d\r\n" % (int(case)+1, wins)
            print line,
            fh.write(line)
    

if __name__ == '__main__':
    main()
