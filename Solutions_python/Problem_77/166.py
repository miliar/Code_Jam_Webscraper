from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)
fp = open(os.path.join(directory, files[0]), 'rb')

fp2 = open(os.path.join(directory, '..', 'out4.out'), 'wb')

lines = fp.readlines()
tests = int(lines[0].strip())

for i in range(tests):
    args = map(int, lines[2*i+2].split())

    hits = 0.0
    for k, a in enumerate(args, start=1):
        if a != k:
            hits += 1.0
    print('Case #%d: %.7f' % (i+1, hits), file=fp2)

fp.close()
fp2.close()
