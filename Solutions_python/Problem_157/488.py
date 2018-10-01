#! /usr/bin/env python3
import sys

# build multiplication table
mul = {"11":"1", "ij":"k", "jk":"i", "ki":"j"}
for a in "ijk": mul[a+a]="-1"

def Neg(q):
    return q[1:] if q[0] == '-' else '-'+q


def HeurMul(a,b):
    """heuristic multiplication"""
    if a+b in mul:
        return mul[a+b]
    if a=='1': return b
    if b=='1': return a
    if a[0]=='-': return Neg(HeurMul(Neg(a),b))
    if b[0]=='-': return Neg(HeurMul(a,Neg(b)))
    return Neg(HeurMul(b,a))

for a in "1 i j k -1 -i -j -k".split():
    for b in "1 i j k -1 -i -j -k".split():
        mul[a+b] = HeurMul(a,b)


number_of_test_cases = int(sys.stdin.readline())

def test_ijk(s,X):
    r = '1'
    for t in s:
        r = mul[r+t]
    rr = '1'
    for t in range(X%8):
        rr = mul[rr+r]
    if rr != '-1':
        return 'NO'
    r = '1'
    needed = 'i'
    for t in s*min(8,X):
        r = mul[r+t]
        if r == needed:
            if needed=='i':
                r, needed = '1','j'
                continue
            assert needed=='j'
            return 'YES'
    return 'NO'



for test_no in range(1, number_of_test_cases+1):
    L, X = map(int, sys.stdin.readline().split())
    ijk = sys.stdin.readline().split()[0]
    print("Case #{}: {}".format(test_no, test_ijk(ijk,X)))

