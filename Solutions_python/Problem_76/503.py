from __future__ import division, print_function

import re, sys

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        tests = []
        for index in xrange(count):
            f.readline() # Don't care
            tline = [int(x) for x in f.readline().strip().split()]
            tests.append((index + 1, tline))
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %s" % (r.index, r.res), # real result line
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, res):
        self.index = index
        self.res = res

    def __str__(self):
        return "Result #%d: %s" % (self.index, self.res)

def compare_files(expected, got):
    with open(expected, 'rb') as i1:
        with open(got, 'rb') as i2:
            line = 1
            while True:
                try:
                    l1 = i1.next().rstrip()
                except StopIteration:
                    l1 = None
                try:
                    l2 = i2.next().rstrip()
                except StopIteration:
                    l2 = None
                    
                if l1 != l2:
                    print("At line %d, expected:" % line)
                    print(l1)
                    print("  but got:")
                    print(l2)
                    return False
                elif l1 is None:
                    break
                line += 1
    return True

def solve_one(test, verbose=False):
    index = test[0]
    print("Solving case #%d" % index)
    candies = test[1]
    if verbose:
        print("Candies: %s" % candies)

    tot = 0
    for c in candies:
        tot = tot ^ c
    if tot != 0:
        return Result(index, 'NO')

    sean = min(candies)
    patrick = sum(candies) - sean
    
    return Result(index, patrick)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test, verbose=verbose) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(check_file, out_file):
            print("Results match expected")

MY_FILES = ["sampleC"]
    
    
def main(filename=None):
    if filename is None:
        for f in MY_FILES:
            print("Solving %s" % f)
            solve(f + ".in", f + ".out", f + ".check", verbose=True)
            print("------------")
    else:
        real_filename = filename if not filename.endswith(".in") else filename[:-len(".in")]
        solve(real_filename + ".in", real_filename + ".out", verbose=False)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        main()
    else:
        main(sys.argv[1])
