import math

fin = open('B-small-attempt1.in', 'r')
fout = open('B-small-attempt1.out', 'w')

t = int(fin.readline())
for i in xrange(1, t + 1):
    ac, aj = [int(ssss) for ssss in fin.readline().strip().split(" ")]
    minute = [0] * 1440
    sum2 = 0
    sum1 = 0
    c = []
    j = []
    for k in range(ac):
        x, y = [int(ssss) for ssss in fin.readline().strip().split(" ")]
        c.append((x,y))
        for u in range(x, y):
            minute[u] = 1
        sum1 += y - x
    for k in range(aj):
        x, y = [int(ssss) for ssss in fin.readline().strip().split(" ")]
        j.append((x, y))
        for u in range(x, y):
            minute[u] = 2
        sum2 += y - x
    c = sorted(c, key=lambda x: x[0])
    j = sorted(j, key=lambda x: x[0])

    tmp = []
    mark = True
    if ac > 1:
        for ii in range(ac):
            s = c[ii][1] % 1440
            t = c[(ii + 1) % ac][0]
            jj = s
            while jj != t:
                if minute[jj] != 0:
                    mark = False
                    break
                jj = (jj + 1) % 1440
            if mark:
                tmp.append((t + 1440 - s) % 1440)
        tmp = sorted(tmp)
        for ii in tmp:
            if sum1 + ii <= 720:
                sum1 += ii
                ac -= 1
            else:
                break

    tmp = []
    mark = True
    if aj > 1:
        for ii in range(aj):
            s = j[ii][1] % 1440
            t = j[(ii + 1) % aj][0]
            jj = s
            while jj != t:
                if minute[jj] != 0:
                    mark = False
                    break
                jj = (jj + 1) % 1440
            if mark:
                tmp.append((t + 1440 - s) % 1440)
        tmp = sorted(tmp)

        for ii in tmp:
            if sum2 + ii <= 720:
                sum2 += ii
                aj -= 1
            else:
                break

    print>>fout, "Case #{}: {}".format(i, 2 * max(ac, aj))

fin.close()
fout.close()
