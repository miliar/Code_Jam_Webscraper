test_input = """3
1 4
10 120
100 1000"""

import math

def check(snn):
    mid = len(snn)/2
    for i in range(mid):
        if snn[i] != snn[len(snn) - mid]:
            return False
    return True

def solve(case):
    a, b = case
    a_ = int(math.ceil(math.sqrt(a)))
    b_ = int(math.ceil(math.sqrt(b)))
    count = 0
    for n in range(a_, b_+1):
        if check(str(n)):
            nn = n*n
            if nn <= b:
                snn = str(nn)
                if check(snn):
                    count += 1
    return count

def run(input):
    lines = input.split('\n')
    no = int(lines[0])
    lines = lines[1:]
    for idx, x in enumerate(lines):
        if x:
            print "Case #%d: %d"%(idx+1, solve(map(int, x.split())))

if __name__ == '__main__':
    import sys
    input = sys.argv[1]
    run(open(input).read())
