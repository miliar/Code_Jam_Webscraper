import sys
filename = sys.argv[1]

in_f = open(filename)
T = int(in_f.readline().strip())

tests = [x.strip().split() for x in in_f.readlines()]
for t in xrange(len(tests)):
    m = int(tests[t][0])
    curr_a = 0
    need = 0
    for n in xrange(len(tests[t][1])):
        deficit = n - curr_a - need
        if (deficit > 0):
            need += deficit
        curr_a += int(tests[t][1][n])
    print "Case #{}: {}".format(t + 1, need)
