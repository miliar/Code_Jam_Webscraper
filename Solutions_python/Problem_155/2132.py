import sys
from collections import deque


with open(sys.argv[1], 'r') as fp:
    data = fp.readlines()


cases = data.pop(0)
results = list()

for idx, test_case in enumerate(data, start=1):
    test_case = test_case.strip()
    smax, people = test_case.split(" ")

    accum = 0
    extras = 0
    for shyness, c in enumerate(people, start=1):
        num = int(c)
        accum += num

        if accum < shyness:
            these_extras = shyness - accum
            accum += these_extras
            extras += these_extras

    outp = "Case #%d: %d\n" % (idx, extras)
    results.append(outp)
    print outp,


with open(sys.argv[1].split(".")[0] + '.out', 'w') as fp:
    fp.writelines(results)