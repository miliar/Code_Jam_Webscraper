import re,sys

numCases = int(sys.stdin.readline())
cases = []

for n in range(numCases):
    hold = re.split(r'\s+',sys.stdin.readline().strip())
    C = int(hold[0])
    D = int(hold[1])
    pairs = []
    for c in range(C):
        pairs.append(map(int,re.split(r'\s+',sys.stdin.readline().strip())))
    
    cases.append([C,D,pairs])
    

def needmove(v,d):
    start = v[0] - d
    out = False
    for vendor in v:
        if vendor - start < d:
            out = True
            break
        else:
            start = vendor
    return out


def move(v,d):
    v[0] = v[0] - 0.5
    v[len(v) - 1] = v[len(v) - 1] + 0.5
    
    c = 1
    for ven in v[1:len(v) - 1]:
        left = v[c - 1]
        right = v[c + 1]

        if ven - left > right - ven:
            v[c] = v[c] - 0.5
        else:
            v[c] = v[c] + 0.5
        c = c + 1
    return v

def time(d,pairs):
    vendors = []
    for pair in pairs:
        for v in range(pair[1]):
            vendors.append(pair[0])
    vendors.sort()
    t = 0.0
    while needmove(vendors,d):
        vendors = move(vendors,d)
        t = t + 0.5
    return t

i = 1
for case in cases:
    print "Case #" + str(i) + ": " + str(time(case[1],case[2]))
    i = i + 1
