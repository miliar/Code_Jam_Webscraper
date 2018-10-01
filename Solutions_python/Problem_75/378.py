import sys

def gen_combs(vec):
    ret = {}
    for comb in vec:
        tmp = ret.setdefault(comb[0], {})
        tmp[comb[1]] = comb[2]

        tmp = ret.setdefault(comb[1], {})
        tmp[comb[0]] = comb[2]
    return ret

def gen_defs(vec):
    ret = {}
    for x in vec:
        tmp = ret.setdefault(x[0], set())
        tmp.add(x[1])
        
        tmp = ret.setdefault(x[1], set())
        tmp.add(x[0])

    return ret

def solve(line):
    seq = line.split()

    c = int(seq[0])
    combs = gen_combs(seq[1:1 + c])

    offset = 1 + c
    d = int(seq[offset])
    defs = gen_defs(seq[offset + 1: offset + 1 + d])

    offset = offset + 1 + d
    size = int (seq[offset])
    string = seq[offset + 1]

    ret = string[0]
    for ind in range(1, size):
        ch = string[ind]

        if ret == '':
            ret = ret + ch
            continue

        last = ret[len(ret) - 1]
        if ch in combs and last in combs[ch]:
            ret = ret[:-1] + combs[ch][last]
            continue

        if ch in defs:
            bb = False
            for let in ret:
                if let in defs[ch]:
                    bb = True
            if bb:
                ret = ''
                continue

        ret += ch

    return parse(ret)

def parse(vec):
    ret = ''
    for ind in range(len(vec)):
        ret += vec[ind]
        if ind < len(vec) - 1:
            ret += ', '
    return '[' + ret + ']'

def main():
    if len(sys.argv) != 2:
        raise ValueError

    file = open(sys.argv[1], 'r')

    n_tests = int(file.readline())
    for test in range(1, n_tests + 1):
        answer = solve(file.readline())
        print "Case #{0}: {1}".format(test, answer)

main()
