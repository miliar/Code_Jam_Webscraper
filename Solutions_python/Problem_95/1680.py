import sys

#lines = sys.stdin.readlines()

#slova = []
#for line in lines:
#    line = line.rstrip().split('|')
#    for i in zip(line[0],line[1]):
#        slova.append(i)
#slova.append(('q','z'))
#slova.append(('z','q'))

#slova = sorted(set(slova))

#for i,j in slova:
#    print i,j

s = open('slova.txt', 'r')
slova = s.readlines()

zamjena = {}
for slovo in slova:
    slovo = slovo.rstrip().split(',')
    zamjena[slovo[0]] = slovo[1]

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    line = ''.join(map(lambda c: zamjena[c], sys.stdin.readline().rstrip()))
    print 'Case #'+str(i+1)+': '+line
