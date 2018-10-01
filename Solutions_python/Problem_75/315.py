#!/usr/bin/env python

import array
import math
import sys
import fractions
import copy

# Print the result
def print_res(t):
    s = "["
    for e in t:
        s += e + ", "

    if (len(t) > 0):
        s = s[:-2] + "]"
    else:
        s += "]"

    return s

# If can be combined, return the new letter
def can_combine(e1, e2, combine):
    if (combine.has_key(e1)):
        l = combine[e1]
        for (efrom, eto) in l:
            if efrom == e2:
                return eto
    return None

# Return if opposed
def is_opposed(opposed, elements, c):
    if opposed.has_key(c):
        l = opposed[c]
        for e in l:
            if e in elements:
                return True
    return False

# Compute result
def result(combine, opposed, invoke):
    elements = []

    for x in xrange(0, len(invoke)):
        c = invoke[x]

        if (len(elements) > 0):
            # combine
            c2 = elements[len(elements) - 1]
            eto = can_combine(c, c2, combine)
            if eto:
                elements[len(elements) - 1] = eto
            # if not combined, maybe opposed ?
            else:
                if is_opposed(opposed, elements, c):
                    elements = []
                else:
                    elements.append(c)
        else:
            elements.append(c)

    return elements

# Nb tests
T = int(raw_input())
sys.stderr.write(str(T) + " test to compute\n")

# Process tests
for x in xrange(1, T + 1):
    sys.stderr.write("Load input of test " + str(x) +  "...\n")

    i = 0
    line = raw_input().split(" ")

    combine = {}
    C = int(line[i])
    i += 1
    for y in xrange(1, C + 1):
        s = line[i]
        i += 1
        if not combine.has_key(s[0]):
            combine[s[0]] = []
        combine[s[0]].append((s[1], s[2]))
        if not combine.has_key(s[1]):
            combine[s[1]] = []
        combine[s[1]].append((s[0], s[2]))

    opposed = {}
    D = int(line[i])
    i += 1
    for y in xrange(1, D + 1):
        s = line[i]
        i += 1
        if not opposed.has_key(s[0]):
            opposed[s[0]] = []
        opposed[s[0]].append(s[1])
        if not opposed.has_key(s[1]):
            opposed[s[1]] = []
        opposed[s[1]].append(s[0])

    # ignore the number of chars
    i += 1
    elements = line[i]

    #print combine
    #print opposed
    #print elements

    y = result(combine, opposed, elements)
    print "Case #" + str(x) + ": " + print_res(y)
    sys.stderr.write("\n")
