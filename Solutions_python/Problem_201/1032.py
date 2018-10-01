import re
from collections import Counter

def splitAll(slots):
    nextset = Counter()
    for size, count in slots.items():
        for newsize in chop(size):
            nextset[newsize] += count
    return nextset

def chop(size):
    if size == 0: return [0,0]
    if size %2==1:
        return [int((size - 1)/2)]*2
    else:
        return [int(size/2), int(size/2 - 1)]

def solve(representation):
    N, K = representation

    print(N, K)

    slots = Counter()
    slots[N] = 1
    tot = 0
    step = 0
    while tot + 2**step < K:
        slots = splitAll(slots)
        tot += 2**step
        step += 1
    keys = sorted(slots.keys(), reverse=True)
    for size in keys:
        tot += slots[size]
        if tot >= K:
            return '{} {}'.format(chop(size)[0], chop(size)[1])

    return 'wack'


def getprob(content):
    prob = content[0]
    del content[0]
    return prob


def parseprob(text):
    match = re.match("(\d+) (\d+)", text)
    if not match:
        print('regular expression is fucked up')
        exit(1)
    N = int(match.group(1))
    K = int(match.group(2))
    return N, K


def readAndSolve():
    d = "C:\\Users\\dave\\Downloads\\"
    infile = "C-small-2-attempt0.in"
    content = []
    with open(d + infile) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    numprobs = int(content[0])
    del content[0]

    lines = []
    for pnum in range(numprobs):
        prob = getprob(content)
        representation = parseprob(prob)
        solved = solve(representation)
        str = 'Case #{}: {}'.format(pnum + 1, solved)
        print(str)
        lines.append(str)

    outfname = infile.replace(".in", ".out")
    outfile = "C:\\Users\\dave\\PycharmProjects\\codejam_2017_qualifier\\" + outfname
    f = open(outfile, 'w')
    print('\n'.join(lines), file=f)
    f.close()


readAndSolve()
