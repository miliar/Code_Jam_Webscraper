# -*- coding: utf-8 -*-


def doClear(opposed, elements):
    if opposedTo(opposed, elements[-1]) in elements:
        return []
    return elements

def doCombo(combos, elements):
    if len(elements) < 2:
        return elements
    combination = getCombo(combos, elements[-1], elements[-2])
    elements = elements[:-2]
    elements.extend(combination)
    return elements

#dictionary for speed
def opposedTo(opposed, element):
    for i in range(len(opposed)):
        if opposed[i][0] == element:
            return opposed[i][1]
        if opposed[i][1] == element:
            return opposed[i][0]

def getCombo(combos, a, b):
    for i in range(len(combos)):
        if combos[i][0] == a and combos[i][1] == b:
            return [combos[i][2]]
        if combos[i][0] == b and combos[i][1] == a:
            return [combos[i][2]]
    return [b, a]

data = open('B.in', 'r').read().split('\n')
output = open('B.out', 'w')

T = int(data.pop(0))

for t in range(T):
    line = data.pop(0).split(' ')
    C = int(line.pop(0))
    combos = []
    for i in range(C):
        sline = line.pop(0)
        combos.append((sline[0], sline[1], sline[2]))
    D = int(line.pop(0))
    opposed = []
    for i in range(D):
        sline = line.pop(0)
        opposed.append((sline[0], sline[1]))
    N = int(line.pop(0))
    invoked = list(line.pop(0))
    elementList = []

    while invoked:
        elementList.append(invoked.pop(0))
        elementList = doCombo(combos, elementList)
        elementList = doClear(opposed, elementList)

    ans = '[' + ', '.join(elementList) + ']'
    print 'Case #' + str(t+1) + ': ' + ans
    output.write('Case #' + str(t+1) + ': ' + ans+'\n')
