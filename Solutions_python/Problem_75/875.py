#!/usr/bin/env python

aaa = """5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
3 EEZ ABC YTR 2 QE KL 7 QEEEERA
"""



def read_input(D):
    D = D.strip().split("\n")[1:]
    D = [d.split() for d in D]
    R = []
    for d in D:
        r = []
        comb = int(d[0])
        C = d[1:comb + 1]
        cd = {}
        for c in C:
            cd[c[:2]] = c[-1]
        r.append(cd)
        oppo = int(d[comb + 1])
        r.append(d[1 + comb + 1:comb + oppo + 1 + 1])
        r.append(d[-1])
        R.append(r)
    return R

def apply_comb(stack,comb):
    if not stack or len(stack) < 2:
        return
    a,b = stack[-2:]
    ab = a+b
    ba = b+a
    if ab in comb:
        del stack[-2:]
        stack.append(comb[ab])
    elif ba in comb:
        del stack[-2:]
        stack.append(comb[ba])
    else:
        return
    apply_comb(stack,comb)

def apply_oppo(stack,oppo):
    for a,b in oppo:
        if a in stack and b in stack:
            del stack [:]
            return

def run(r):
    cmd = list(r[-1])
    comb = r[0]
    oppo = r[1]
    stack = [cmd.pop(0)]
    while cmd:
        stack.append(cmd.pop(0))
        apply_comb(stack,comb) 
        apply_oppo(stack,oppo)
    return "[" + ", ".join(stack) + "]"

def process(D):
    k = 1
    for d in D:
        r = run(d)
        print "Case #%d: %s"% (k, r)
        k+=1


inp = open("c:\\downloads\\B-large.in").read()
D = read_input(inp)
process(D)

