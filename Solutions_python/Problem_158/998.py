fin = open('D-small-attempt0.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

two = [12, 14, 21, 22, 23, 24, 32, 34, 41, 42, 43, 44]
three = [23, 32, 33, 34, 43]
four = [34, 43, 44]

for i in xrange(t):
    x, r, c = map(int, fin.readline().split())
    if x == 1:
        result = 2
    elif x == 2:
        if r*10+c in two:
            result = 2
        else:
            result = 1
    elif x == 3:
        if r*10+c in three:
            result = 2
        else:
            result = 1
    else:
        if r*10+c in four:
            result = 2
        else:
            result = 1
    
    if result == 1:
        fout.write('Case #' + str(i + 1) + ': RICHARD\n')
    else:
        fout.write('Case #' + str(i + 1) + ': GABRIEL\n')

fout.close()
