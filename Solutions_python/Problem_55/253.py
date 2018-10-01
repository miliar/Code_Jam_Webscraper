import sys
out = file('ans','w')
if __name__ == '__main__':
    test = int(sys.stdin.readline())
    c = 1
    while test>0:
        test -=1
        info = sys.stdin.readline()
        info = info.split(' ')
        R = int(info[0])
        k = int(info[1])
        N = int(info[2])
        info = sys.stdin.readline()
        info = info.split(' ')
        line1 = []
        line2 = []
        for i in info:
            line1.append(int(i))
        cost = 0
        for i in range(R):
            total = 0
            while len(line1)>0 and total+line1[0]<= k:
                total += line1[0]
                line2.append(line1[0])
                line1 = line1[1:]
            cost += total
            line1 += line2
            line2 = []
        print 'Case #',c,': ',cost
        out.writelines('Case #%d: %d\n'%(c,cost))
        c += 1