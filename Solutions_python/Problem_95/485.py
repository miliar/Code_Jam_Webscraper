import sys

with open(sys.argv[1]) as f:
    n_cases = f.readline()
    cases = [line[:-1] for line in f]

MAPPING = {'z': 'q', 'q': 'z'}

with open(sys.argv[2]) as f:
    plain = [line[:-1] for line in f]

with open(sys.argv[3]) as f:
    crypt = [line[:-1] for line in f]

for i, _ in enumerate(plain):
    for j, _ in enumerate(plain[i]):
        MAPPING[crypt[i][j]] = plain[i][j]

for i, case in enumerate(cases):
    print "Case #%d: %s" % (i + 1, "".join([MAPPING[c] for c in case]))
