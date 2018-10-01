#!/usr/bin/python

def to_int(l):
    result = []
    for i in l:
        result.append(int(i))
    return result

def parse(input):
    lines = input.split("\n")
    index = 0
    case = []
    line = lines[0].strip()
    T = int(line)
    index = 1
    cases = []
    for i in range(T):
        line = lines[index].strip()
        n = int(line)
        index += 1
        line = lines[index].strip()
        a = to_int(line.split(" "))
        index += 1
        line = lines[index].strip()
        b = to_int(line.split(" "))
        d = {}
        d['a'] = a
        d['b'] = b
        cases.append(d)
        index += 1
    return cases


def product(a,b):
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    return sum

def solve(case):
    a = case['a']
    b = case['b']

    a.sort()
    b.sort(reverse=True)

    return product(a,b)


f = open('input.txt','r')
input = f.read()
f.close()
cases = parse(input)
o = open('output.txt','w')
case_number = 1
for case in cases:
    print case
    result = solve(case)
    o.write('Case #%s: %s\n' % (case_number, result))
    case_number += 1
