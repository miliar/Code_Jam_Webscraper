import sys

def do_case(number, line):
    tokens = list(line.split())
    c = int(tokens[0])
    combination = {}
    del tokens[0]
    for combostring in tokens[:c]:
        if combostring[0] <= combostring[1]:
            combination[(combostring[0], combostring[1])] = combostring[2]
        else:
            combination[(combostring[1], combostring[0])] = combostring[2]
    del tokens[:c]
    d = int(tokens[0])
    del tokens[0]
    opposing = []
    for opposstring in tokens[:d]:
        if opposstring[0] <= opposstring[1]:
            opposing.append((opposstring[0], opposstring[1]))
        else:
            opposing.append((opposstring[1], opposstring[0]))
    del tokens[:d]
    n = int(tokens[0])
    del tokens[0]
    invokation = list(tokens[0])
    elements = []
    while invokation:
        nextel = invokation[0]
        if not elements:
            # print(invokation, elements, 'BEFORE EMPTYLIST')
            elements.append(nextel)
            del invokation[0]
            # print(invokation, elements, 'AFTER EMPTYLIST')
            continue
        lastel = elements[-1]
        if nextel > lastel:
            nextel, lastel = lastel, nextel
        if (nextel, lastel) in combination:
            elements.pop()
            # print(invokation, elements, 'BEFORE COMBINATION')
            elements.append(combination[(nextel, lastel)])
            del invokation[0]
            # print(invokation, elements, 'AFTER COMBINATION')
        else:
            suck = False
            for el in elements:
                nextel = invokation[0]
                if nextel > el:
                    nextel, el = el, nextel
                if (nextel, el) in opposing:
                    # print(invokation, elements, 'BEFORE OPPOSITION')
                    elements = []
                    del invokation[0]
                    # print(invokation, elements, 'AFTER OPPOSITION')
                    suck = True
                    break
            if suck:
                continue
            # print(invokation, elements, 'BEFORE INERT')
            elements.append(invokation[0])
            del invokation[0]
            # print(invokation, elements, 'AFTER INERT')
    print("Case #{}: [{}]".format(number + 1, ', '.join(elements)))

with sys.stdin as inputfile:
    iterinput = iter(inputfile)
    t = iterinput.__next__()
    for caseinput in enumerate(iterinput):
        do_case(*caseinput)
