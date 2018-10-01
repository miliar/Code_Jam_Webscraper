#!/usr/bin/python36

from functools import reduce

def minimum_time(horseiter, dest_distance: float):
    horseiter = iter(horseiter)
    return reduce(max,
                  ((dest_distance - pos) / velocity \
                   for pos, velocity in horseiter),
                  0)

def annies_speed(horseiter, dest_distance):
    return dest_distance / minimum_time(horseiter, dest_distance)

def single_test(tnum, infile, outfile):
    dest_distance, num_horses = (
        int(x) for x in infile.readline().strip().split()
    )
    horseiter = (tuple(int(x) for x in infile.readline().strip().split())
                 for hnum in range(0, num_horses))
    print(f'Case #{tnum}: {annies_speed(horseiter, dest_distance)}',
          file=outfile)

def all_tests(infile, outfile):
    num_tests = int(infile.readline().strip())
    for tnum in range(0, num_tests):
        single_test(tnum + 1, infile, outfile)

if __name__ == '__main__':
    import sys
    all_tests(sys.stdin, sys.stdout)
