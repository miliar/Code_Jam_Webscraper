# coding: utf-8

"""
File Fix-it
"""
def check(field, path):
        directories = path.split('/')
        i = 0
        ups = ''
        for d in directories:
                ups += d
                if i >= len(field):
                        field.append([])
                if (ups not in field[i]):
                        field[i].append(ups)


def count(field, n, i):
        num = 0
        for level in field:
               num += len(level)
        return "Case #" + str(i) + ": " + str(num - n) + '\n'
#        print result,

foutput  = open('A-small.out', 'w')

i = 0
j = 0
k = 0
field = []
for line in open('A-small-attempt0.in', 'r'):
        i += 1
        if i == 1:
                t = line[:-1]
                continue
        item = line[:-1].split()
        if len(item) == 2:
                if len(field) > 0:
                        k += 1
#                        print count(field, n, k),
                        foutput.write(count(field, n, k))
                n = int(item[0])
                m = int(item[1])
                field = []
                j = 0
                continue
        check(field, item[0][1:])
        j += 1
        if j < n:continue
k += 1
#print count(field, n, k),
foutput.write(count(field, n, k))

foutput.close()
