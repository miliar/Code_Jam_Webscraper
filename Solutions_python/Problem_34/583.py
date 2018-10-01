import sys

L = 0
D = 0
N = 0

X = 0

line = sys.stdin.readline()

line = line.split()

L = int(line[0])
D = int(line[1])
N = int(line[2])

dic = {}
for x in xrange(0,D):
    d = dic
#   print d
    line = sys.stdin.readline().strip()
#    print line
    for x in xrange(0,len(line)):
#        print d
        if d.has_key(line[x]):
            d = d[line[x]]
        else:
#           print 'cria', line[x]
            d.update({line[x]:{}})
            d = d[line[x]]
#print dic
cont = 0

def test(list, dic, s=0):

#    print list, dic

    if len(list) == 0:
#        print "CONTA"
        return 1

    list2 = []
    for i in list:
        list2.append(i)

    ini = list2.pop(0)

    total = 0
    for i in ini:
#        print i
        if dic.has_key(i):
#            print "SIM", i
            total += test(list2, dic[i])
    return total

for y in xrange(0,N):
    line = sys.stdin.readline().strip()
#    print line

    r = []
    x = 0
    while x < len(line):
        if line[x] == '(':
            r.append([])
            x+=1
            while line[x] != ')':
                r[-1].append(line[x])
                x += 1

        if line[x]  != ')':
            r.append([line[x]])
        x+=1
#    print r

    res = test(r, dic)
    print "Case #%d: %d" %(y+1,res)

