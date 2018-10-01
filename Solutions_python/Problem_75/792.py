#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

def pair_to_str(pair):
    return '%s%s' % (pair[0],pair[1]) 

def combine(C,element_list):
    if len(element_list) < 2:
        return
    pair = pair_to_str(element_list[-2:])
    if pair in C:
        e = C[pair]
        element_list[-2:] = [e]
        return True
    return False

def oppose(D,element_list):
    if len(element_list) < 2:
        return
    e = element_list[-1]
    if e in D:
        for opposed in D[e]:
            if opposed in element_list[:-1]:
                element_list[:] = []

def solve(Cs,Ds,bases):
#    print Cs
#    print Ds
    
    C = {}
    for cs in Cs:
        pair = cs[0:2]
        e = cs[2]
        p = u'%s' % pair
        sp = bytearray(pair)
        sp.reverse()
        pr = sp.decode()
        C[p] = e
        C[pr] = e
#    print C
    
    D = {}
    for ds in Ds:
        def add_or_create(M,key,e):
            if key in M:
                M[key].append(e)
            else:
                M[key] = [e]
        
        add_or_create(D, ds[0], ds[1])
        add_or_create(D, ds[1], ds[0])
#    print D
    
    bases = list(bases)
    
    element_list = []
    while len(bases) > 0:
        base_to_invoke = bases.pop(0)
        element_list.append(base_to_invoke)
        
        combined = True
        while (combined):
            combined = combine(C,element_list)

        oppose(D,element_list)
        
    return element_list

T = int(input.readline())
assert 1<=T and T<=100

for t in range(1,T+1):
    S = input.readline().split(' ')
    S = [s.strip() for s in S]

    C = int(S[0])
    assert 0<=C and C<=36
    Cs = S[1:1+C]
    
    S = S[1+C:] 
    D = int(S[0])
    assert 0<=D and D<=28
    Ds = S[1:1+D]
    
    S = S[1+D:] 
    N = int(S[0])
    assert 1<=N and N<=100
    elementsBase = S[1]
    assert len(elementsBase) == N
    
    elementsFinal = solve(Cs,Ds,elementsBase)
    ef = map(lambda e: str(e), elementsFinal)
    output.write('Case #%s: [%s]\n' % (t,', '.join(ef)))
