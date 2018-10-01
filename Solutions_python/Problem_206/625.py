#!/usr/bin/python

import sys, datetime

def solve(d, n, h):
    h.sort()
    i = 0
    k1, s1 = h[0]
    for k2, s2 in h[1:]:
        if s1 > s2 and (k2 - k1)*s1 < (d - k1)*(s1 - s2):
            k1, s1 = k2, s2
    return float(d*s1)/(d - k1)

def parse(input_file):
    d, n = map(int, input_file.readline().strip().split())
    h = []
    for i in xrange(n):
        h.append(map(int, input_file.readline().strip().split()))
    return (d, n, h)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print "Writing to %s" % sys.argv[2] if output_file else "No output file"
    test_cases = int(input_file.readline().strip())
    print "Test cases:",test_cases
    print '-----------------'
    for tc in xrange(1, test_cases + 1):
        output = "Case #%d: %.6f" % (tc, solve(*parse(input_file)))
        print output
        if output_file:
            output_file.write(output + "\n")
    print '-----------------'
    print "Written to %s" % sys.argv[2] if output_file else "No output file"
    print 'Elapsed time: %s' % (datetime.datetime.now() - start)
    input_file.close()
    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
