#!/usr/bin/env python

def combine(elements, combinations):
    if not len(elements) > 1:
        return elements
    elem1 = elements[len(elements) - 2]
    elem2 = elements[len(elements) - 1]
    for comb in combinations:
        elems = comb[0]
        result = comb[1]
        if elem1 == elems[0]:
            if elem2 == elems[1]:
                return elements[:-2] + result
        elif elem2 == elems[0]:
            if elem1 == elems[1]:
                return elements[:-2] + result
    return elements

def oppose(elements, oppositions):
    for opp in oppositions:
        copy = elements[:]
        if opp[0] in copy:
            copy = copy.replace(opp[0], '', 1)
            if opp[1] in copy:
                return ''
    return elements
    
def invoke(elements, element):
    return elements + element

def construct_combs(inp):
    combs = []
    for s in inp:
        combs.append([(s[0],s[1]),s[2]])
    return combs

def construct_opps(inp):
    opps = []
    for s in inp:
        opps.append((s[0], s[1]))
    return opps

def process_input(inp):
    result = []
    preprocess = inp.split()
    combs = int(preprocess[0])
    preprocess = preprocess[1:]
    comblist = []
    while combs > 0:
        comblist.append(preprocess[0])
        preprocess = preprocess[1:]
        combs -= 1
    result.append(comblist)
    opps = int(preprocess[0])
    preprocess = preprocess[1:]
    oppslist = []
    while opps > 0:
        oppslist.append(preprocess[0])
        preprocess = preprocess[1:]
        opps -= 1
    result.append(oppslist)
    result.append(preprocess[1:])
    return result

def apply(combinations, oppositions, inp):
    result = ''
    for c in inp:
        result += c
        result = combine(result, combinations)
        result = oppose(result, oppositions)
    return result

def pretty_list(elems):
    if elems == '':
        return '[]'
    result = '['
    for e in elems:
        result += e + ', '
    return result[:-2] + ']'

def main():
    results = []
    cases = input()
    for case in range(cases):
        inp = raw_input()
        processed = process_input(inp)
        combinations = construct_combs(processed[0])
        oppositions = construct_opps(processed[1])
        invocations = processed[2][0]
        result = apply(combinations, oppositions, invocations)
        results.append(pretty_list(result))
    for case in range(cases):
        print 'Case #' + str(case + 1) + ': ' + results[case]

if __name__ == '__main__':
   main()
        
