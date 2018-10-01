import sys
t = int(sys.stdin.readline())
for ti in range(t):
    case = sys.stdin.readline()
    parts = case.split()
    c = int(parts[0])
    combines = parts[1:1+c]
    d = int(parts[1+c])
    destroys = parts[2+c:2+c+d]
    n = int(parts[2+c+d])
    sequence = parts[3+c+d]

    #print (combines, destroys, sequence)

    reactions = dict((formula[0]+formula[1], formula[2]) for formula in combines)
    reactions.update(dict((formula[1]+formula[0], formula[2]) for formula in combines))
    #print reactions

    stack = []
    for letter in sequence:
        stack.append(letter)
        end = ''.join(stack[-2:])
        if end in reactions:
            stack = stack[:-2]
            stack.append(reactions[end])

        for pair in destroys:
            if pair[0] in stack and pair[1] in stack:
                stack = []

    print 'Case #{0}: {1}'.format(ti+1, '[' + ', '.join(stack) + ']')
