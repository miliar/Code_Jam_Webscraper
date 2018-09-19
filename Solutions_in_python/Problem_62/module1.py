fin = open('small.in')
fout = open('result.out', 'w')
data = fin.readlines()
for x in xrange(len(data)):
    data[x] = (data[x])[:-1]
cases = int(data[0])
case = 1
number = 1
while case < len(data):
    num = int(data[case])
    lines = []
    for x in xrange(num):
        temp = (data[x + case + 1]).split()
        lines += [(int(temp[0]), int(temp[1]))]
    case += num
    ans = 0
    for x in xrange(len(lines)):
        for y in xrange(x + 1, len(lines)):
            if lines[x][0] > lines[y][0] and lines[x][1] < lines[y][1]:
                ans += 1
            if lines[x][0] < lines[y][0] and lines[x][1] > lines[y][1]:
                ans += 1
    case += 1
    print >>fout, 'Case #' + str(number) + ':', str(ans)
    number += 1
fin.close()
fout.close()
