def writer(op, case, toprint):
    op.write('Case #'+str(case+1)+': '+str(toprint)+'\n')

def check(a,b):
    if a in b*2:
        return True
    return False

ip = open('C-small-attempt0.in')
op = open('C-out.out', 'w')
n = int(ip.readline())
##n = 1
for a in xrange(n):
    small, large = map(int, str(ip.readline()).split())
##    small, large = 10000, 90000
    count = 0
    for i in xrange(small, large+1):
        for j in xrange(i+1, large+1):
            count += int(check(str(i),str(j)))
    writer(op,a,count)
ip.close()
op.close()
