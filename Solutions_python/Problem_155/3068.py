#!/usr/bin/env python2.7

from sys import argv

if len(argv) != 2:
    print 'no file'

else:
    inputfile = open(argv[1], 'r')
    outputfile = open('result', 'w')

    n = inputfile.readline().split('\n', 1)
    n = int(n[0])  # convertir chaine
    print n, ':nombre de tours'

    for i in range(0, n):
        line = inputfile.readline().split('\n', 1)
        line = line[0].split(' ', 1)
        print line[0], 'et', line[1]
        count = 0
        add = 0
        j = 0
        for element in line[1]:  # line contient les digits, count pour compter
        # les spectateurs.
            if count < j:
                add += j - count
                count = j
            count += int(element)
            j += 1

        a = 'Case #' + str(i + 1) + ': ' + str(add)
        # + concatenation (pas d'espaces).
        print a
        outputfile.write(a + '\n')

    inputfile.close()
    outputfile.close()
