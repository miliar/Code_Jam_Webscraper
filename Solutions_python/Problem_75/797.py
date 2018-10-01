'''
Created on May 6, 2011

@author: Administrator
'''

with open(r'data\B-large.in') as fhi, open(r'data\B-large.out', 'w') as fho:
    cases = int(fhi.readline())

    for case in range(cases):
        data = fhi.readline().rstrip().split(' ')

        comboCount = int(data.pop(0))

        combos = [[c for c in data.pop(0)] for _ in range(comboCount)]

        fizzleCount = int(data.pop(0))

        fizzles = [[c for c in data.pop(0)] for _ in range(fizzleCount)]

        elementCount = int(data.pop(0))

        elements = data.pop(0)

        stack = []

        for element in elements:
            stack.append(element)

            if len(stack) == 1:
                continue

            for c in combos:
                if c[0:2] == stack[-2:] or list(reversed(c[0:2])) == stack[-2:]:
                    del stack[-2:]

                    stack.append(c[2])

            for f in fizzles:
                if f[0] in stack and f[1] in stack:
                    stack = []

        fho.write('Case #%d: [%s]\n' % (case + 1, ', '.join(stack)))
