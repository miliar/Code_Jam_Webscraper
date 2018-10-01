import sys

def solve(line):
    line = line.split()
    C, line = int(line[0]), line[1:]
    combine = {}
    for i in range(C):
        a = line[i][0]
        b = line[i][1]
        c = line[i][2]
        combine[(a,b)] = c
        combine[(b,a)] = c
    line = line[C:]
    D, line = int(line[0]), line[1:]
    opposed = {}
    for i in range(D):
        a = line[i][0]
        b = line[i][1]
        if a not in opposed:
            opposed[a] = set()
        if b not in opposed:
            opposed[b] = set()
        opposed[a].add(b)
        opposed[b].add(a)
    line = line[D:]
    N, seq = line[0], line[1]
    so_far = []
    elements = {}
    for l in seq:
        if l not in elements:
            elements[l] = 0
        elements[l] += 1
        so_far.append(l)
        if try_combine(so_far, combine, elements):
            continue
        if l not in opposed:
            continue
        for o in opposed[l]:
            if o in elements and elements[o] > 0:
                so_far = []
                elements = {}
                break
    return so_far

def try_combine(l, combine, elements):
    combined = False
    while len(l) >=2 and (l[-1], l[-2]) in combine:
        combined = True
        removed = l[-1], l[-2]
        l[-2] = combine[(l[-1], l[-2])]
        l.pop()
        for item in removed:
            if item not in elements:
                continue
            elements[item] -= 1
    return combined

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        line = raw_input()
        result = solve(line)
        if not result:
            print "Case #%d: []" % i
            continue
        
        sys.stdout.write("Case #%d: [" % i)
        for a in result[:-1]:
            sys.stdout.write(a + ", ")
        sys.stdout.write("%s]\n" % result[-1])
