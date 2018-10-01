#!/usr/bin/env python3
import sys
import os.path
from pathlib import Path


def solve(S, K):
    return check([S], K)


def check(nqueue, K):
    all_happy = "+" * len(nqueue[0])
    count = 0
    done = {}

    while len(nqueue) > 0:
        queue = nqueue
        nqueue = []
        while len(queue) > 0:
            # print(queue)
            pc = queue.pop()
            if pc == all_happy:
                return count
            if pc in done or ''.join(reversed(pc)) in done:
                # print(pc, "already done")
                continue
            done[pc] = True
            for i in range(len(pc) - K + 1):
                flipped = flip(pc, i, K)
                if flipped == all_happy:
                    return str(count + 1)
                nqueue.append(flipped)
        count += 1

    return "IMPOSSIBLE"


def flip(pc, pos, K):
    pancakes = list(pc)
    for i in range(pos, pos + K):
        if pancakes[i] == "-":
            pancakes[i] = "+"
        else:
            pancakes[i] = "-"
    # print('flip:', pc, pos, K, ''.join(pancakes))
    return ''.join(pancakes)


#
# Service functions
#
def get_infile(file=None):
    if file:
        return file, Path(file).stem
    me, ext = os.path.splitext(os.path.basename(sys.argv[0]))
    for postfix in ['-large-practice', '-large', '-small-practice', '-small-attempt', '-sample']:
        files = sorted(Path('.').glob(me + postfix + '*'), reverse=True)
        for file in files:
            if file.suffix == '.txt':
                infile = Path(file.stem)
            else:
                infile = file
            if infile.suffix == '.in':
                return file.name, infile.stem
    raise FileNotFoundError('No input files')


#
# main
#
input_file, stem = get_infile()
print('Input:  {}\nOutput: {}.out\n'.format(input_file, stem))

with open(input_file, "r") as fdin:
    with open(stem + ".out", "w") as fdout:
        T = int(fdin.readline())
        for case_num in range(1, T + 1):
            data= fdin.readline().split()
            S = data[0]
            K = int(data[1])

            result = solve(S, K)

            line = "Case #{:d}: {}\n".format(case_num, result)
            print(line, end='')
            fdout.write(line)
