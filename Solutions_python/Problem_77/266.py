import sys

file_prefix = sys.argv[1]
with open(file_prefix + '.in', 'r') as f_in:
    t = int(f_in.readline())
    with open(file_prefix + '.out', 'w') as f_out: 
        for i in xrange(t):
            f_in.readline()
            x = map(int, f_in.readline().split(' '))
            r = sum(a != b-1 for a, b in enumerate(x))
            f_out.write('Case #%s: %.6f\n' % (i + 1, r))