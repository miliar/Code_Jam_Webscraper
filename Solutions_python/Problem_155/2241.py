#f = open('StandingOvation-test.txt')
#f = open('StandingOvation-small.txt')
f = open('StandingOvation-large.txt')

#outFile = open('StadingOvation-out-test.txt','w')
#outFile = open('StadingOvation-out-small.txt','w')
outFile = open('StadingOvation-out-large.txt','w')

line = f.readline()
case = 1
for l in f:
    sp = l.split()
    m = int(sp[0])
    total = 0
    extra = 0
    count = 0
    for p in sp[1]:
        n = int(p)
        if p > 0:
            if total < count:
                dif = count - total
                extra += dif
                total += dif
            total += n
        count+=1
    outFile.write("Case #{0}: {1}\n".format(case,extra))
    case += 1

f.close()
outFile.close()
