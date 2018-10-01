T = int(raw_input())

for t in range(T):
    line = raw_input().split(' ')

    # Read combo elements
    combo = {}

    C = int(line.pop(0))
    for c in range(C):
        formula = line.pop(0)
        combo[formula[:2]] = formula[2]
        combo[formula[1::-1]] = formula[2]

    # Read opposing elements
    oppos = {}

    D = int(line.pop(0))
    for d in range(D):
        elem = line.pop(0)
        oppos[elem[0]] = elem[1]
        oppos[elem[1]] = elem[0]

    # Process the stack
    stack = ""

    for elem in line[1]:
        # First test combination
        candidate = stack[-1:]+elem
        stack = stack[:-1] + combo.get(candidate, candidate)
        # Now opposing
        if oppos.get(stack[-1], None) in set(stack):
            stack = ''

    print "Case #%d: [%s]" % (t+1, ', '.join(stack))
