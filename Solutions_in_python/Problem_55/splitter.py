import sys
import itertools

NUM_FILES = 2

fname = sys.argv[1]
with open(fname) as file:
    lines = file.readlines()

tests = zip(
    itertools.islice(lines, 1, None, 2),
    itertools.islice(lines, 2, None, 2)
)

tests_per_file = (len(tests) + NUM_FILES) / NUM_FILES
for i in xrange(NUM_FILES):
    start = tests_per_file * i
    stop = start + tests_per_file
    with open(fname + '.%d' % (i+1), 'wb') as file:
        file.write('%d\n' % start)
        for test in itertools.islice(tests, start, stop):
            file.write(''.join(test))
