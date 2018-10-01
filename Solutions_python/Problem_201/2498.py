import heapq
import os
import sys
import time

def solve(line):
    num_stalls, num_people = [int(s) for s in line.split()]
    h = []
    heapq.heappush(h, -num_stalls)
    for i in xrange(num_people):
        
        largest_space = -heapq.heappop(h)
        max_s = largest_space / 2
        min_s = (largest_space-1) / 2
        if max_s:
            heapq.heappush(h, -max_s)
        if min_s:
            heapq.heappush(h, -min_s)
    return '{0} {1}'.format(max_s, min_s)

class Stopwatch(object):
    def __init__(self):
        self.start_ts = time.time()

    def end_and_print(self):
        print '{0}s'.format(time.time() - self.start_ts)


if __name__ == '__main__':
    stopwatch = Stopwatch()
    in_filename = sys.argv[1]
    out_filename = os.path.splitext(in_filename)[0] + '.out'
    with open(in_filename, 'r') as in_f, open(out_filename, 'w') as out_f:
        num_tests = int(in_f.readline())
        for idx, line in enumerate(in_f.readlines()):
            result = 'Case #{0}: {1}'.format(idx + 1, solve(line))
            print result
            out_f.write(result + '\n')
    stopwatch.end_and_print()