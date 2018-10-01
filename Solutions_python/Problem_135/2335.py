import sys
import re

fin = open(sys.argv[1], 'r')
fout = open(re.sub(r'\.\w+$', '.out', sys.argv[1]), 'w')

def out(case, s):
    output = 'Case #' + str(case+1) + ': ' + str(s)
    fout.write(output + '\n')
    print output
    
def mapint(s):
    return map(int, s.split(' '))

for T in xrange(int(fin.readline())):
    first = int(fin.readline()) - 1
    
    s1 = set()
    for i in xrange(4):
        row = mapint(fin.readline())
        if i == first:
            s1 = set(row)
    
    second = int(fin.readline()) - 1
    s2 = set()
    for i in xrange(4):
        row = mapint(fin.readline())
        if i == second:
            s2 = set(row)
    
    res = s1 & s2
    if len(res) > 1:
        out(T, 'Bad magician!')
    elif not res:
        out(T, 'Volunteer cheated!')
    else:
        out(T, list(res)[0])


fout.close()
