fairs = [int(x) for x in open("palisquare.txt", 'r')]
fairs.sort()
fin = open('test.in', 'r')
ncase = int(fin.readline())
for i in range(ncase):
    f, t = [int(x) for x in fin.readline().split()]
    count = 0
    for x in fairs:
        if(x < f):
            continue
        if(x > t):
            break
        count += 1
    print 'Case #%d: %d' %(i+1, count)
