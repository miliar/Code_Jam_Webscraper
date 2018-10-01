#!/usr/bin/env python
import sys

def usage(prog_name):
    print >>sys.stderr, "Usage: %s <input-file>" % prog_name

def snapper(n, k):
    """
    Return the state of snapper n after k clicks when the n snappers
    are chained together and k clicks take place.
    """
    if n < 1 or k < 0:
        raise ValueError("Invalid n or k")
    return k % 2**n == 2**n - 1

def on_or_off(input):
    if input:
        return "ON"
    else:
        return "OFF"

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        input = argv[1]
    except IndexError:
        usage(argv[0])
        return 1

    with open(input) as f:
        num_cases = int(f.readline())
        for line_num, line in enumerate(f):
            case_num = line_num + 1
            n, k = map(int, line.split())
            print "Case #%d: %s" % (case_num, on_or_off(snapper(n, k)))
        assert case_num == num_cases
    return 0

if __name__ == "__main__":
    sys.exit(main())
