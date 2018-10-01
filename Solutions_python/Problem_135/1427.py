fin = open('A-small-attempt0.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for i in xrange(t):
    row = int(fin.readline())
    numbers = None
    for j in xrange(4):
        nmbrs = fin.readline().split()
        if j + 1 == row:
            numbers = nmbrs
    row2 = int(fin.readline())
    for j in xrange(4):
        nmbrs = fin.readline().split()
        if j + 1 == row2:
            result = 0
            for k in xrange(4):
                if nmbrs[k] in numbers:
                    result += 1
                    answer = nmbrs[k]
            if result < 1:
                fout.write('Case #' + str(i + 1) + ': Volunteer cheated!' + '\n')
            elif result == 1:
                fout.write('Case #' + str(i + 1) + ': ' + answer + '\n')
            else:
                fout.write('Case #' + str(i + 1) + ': Bad magician!' + '\n')

fout.close()

