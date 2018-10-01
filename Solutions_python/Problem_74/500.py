from __future__ import division, print_function

import re, sys

def read_input(filename):
    with open(filename, 'rb') as f:
        count = int(f.readline())
        tests = []
        for index in xrange(count):
            tline = f.readline().strip().split()
            tests.append((index + 1, tline))
    return tests

def write_output(filename, results):
    with open(filename, 'wb') as f:
        for r in results:
            print("Case #%d: %d" % (r.index, r.turns), # real result line
                  file=f)

# Example class
class Result(object):
    def __init__(self, index, turns):
        self.index = index
        self.turns = turns

    def __str__(self):
        return "Result #%d: %d" % (self.index, self.turns)

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



def find_next(test, i, col):
    for j in range(1 + (i * 2), len(test), 2):
        if test[j] == col:
            return int(test[j + 1])
    return None

def solve_one(test, verbose=False):
    index = test[0]
    print("Solving case#%d" % index)
    t = 0
    i = 0
    o = 1
    b = 1
    ni = int(test[1][0])
    if verbose:
        print("ni=%d" % ni)
    while i < ni:
        next = test[1][1 + (i * 2)]
        next_orange = find_next(test[1], i, "O")
        next_blue = find_next(test[1], i, "B")
        if verbose:
            print("turn %d, i=%d, next:%s, o:%d->%s, b:%d->%s" % (t, i, next,
                                                                  o, next_orange,
                                                                  b, next_blue))
        if next_orange is not None:
            do = next_orange - o
            if (do > 0):
                o += 1
                if verbose:
                    print("Orange move to %d" % o)
            elif (do < 0):
                o -= 1
                if verbose:
                    print("Orange move to %d" % o)
            elif next == "O":
                # Orange press button
                i += 1
                if verbose:
                    print("Orange press at %d" % o)
            elif verbose:
                print("Orange stay at %d" % o)

        if next_blue is not None:
            db = next_blue - b
            if (db > 0):
                b += 1
                if verbose:
                    print("Blue move to %d" % b)
            elif (db < 0):
                b -= 1
                if verbose:
                    print("Blue move to %d" % b)
            elif next == "B":
                # Blue press button
                i += 1
                if verbose:
                    print("Blue press at %d" % b)
            elif verbose:
                print("Blue stay at %d" % b)
                
        t += 1
    return Result(index, t)

def solve(in_file, out_file, check_file=None, verbose=False):
    tests = read_input(in_file) # put input somewhere
    results = [solve_one(test, verbose=verbose) for test in tests]
    write_output(out_file, results)
    if check_file is not None:
        # File comparison
        if compare_files(check_file, out_file):
            print("Results match expected")

MY_FILES = ["sampleA"]
    
    
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
