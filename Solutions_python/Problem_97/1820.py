'''
Created on Apr 14, 2012

@author: moemen
'''

def debug(*args):
    print " ".join(str(arg) for arg in args)

def r(item): return item[0]

def match(arg):
    item1, item2 = arg
    for i in item1:
        item1 = item1[1:] + item1[0]
#        if '0' in (item1[0], item2[0]): return False
        if item1 == item2: return True
    return False

def process_file(fin, fout):
    cases = int(fin.readline())
    out_str = []
    s = str
    ii = int
    le = len
    for case in xrange(cases):
        A, B = fin.readline().strip('\n').split()
        if A == B or '0' in (A[0], B[0]) or le(A) < 2:
            out_str.append(0)
            continue
        a, b = ii(A), ii(B)
        l = [(str(i), str(j)) for i in range(a, b) for j in range(i + 1, b + 1)]
        out_line = filter(match, l)
        out_str.append(le(out_line))
    for x, s in enumerate(out_str):
        fout.write("Case #{0}: {1}\n".format(x + 1, s))

if __name__ == '__main__':
    from sys import argv
    process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))
