IN = open('input.txt', 'r')

T = int(IN.readline())

for ttt in xrange(1, T + 1):

    line = IN.readline().strip().split()

    combine = {}
    oppose = set()

    C = int(line[0])
    for w in line[1: C + 1]:
        combine[w[0] + w[1]] = w[-1]
        combine[w[1] + w[0]] = w[-1]
    del line[:C + 1]

    D = int(line[0])
    for w in line[1: D + 1]:
        oppose.add(w[0] + w[1])
        oppose.add(w[1] + w[0])
    del line[:D + 1]

    L = []
    for x in line[1]:
        L.append(x)
        if len(L) > 1 and L[-1] + L[-2] in combine:
            L[-2:] = combine[L[-1] + L[-2]]
        else:
            for y in L[:-1]:
                if x + y in oppose:
                    L = []
                    break

    from sys import stdout

    stdout.write('Case #{}: ['.format(ttt))

    for i in xrange(len(L)):
        stdout.write('{}'.format(L[i]))
        if i < len(L) - 1:
            stdout.write(', ')
    stdout.write(']\n')
