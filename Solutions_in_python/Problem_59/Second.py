ls = []

def addd(s):
    tp = s.split('/')
    lss = ['']
    for x in xrange(len(tp) - 1):
        lss += [lss[x] + '/' + tp[x + 1]]
    return lss

def check(s, xs):
    ans = 0
    tp = addd(s)
    for x in tp:
        if x not in xs:
            ans += 1
            xs += [x]
    return ans

fin = open('small.in')
fout = open('result.out', 'w')
data = fin.readlines()
for x in xrange(len(data)):
    data[x] = data[x][:-1]
case = int(data[0])
cnt = 1
z = 1
while cnt < len(data):
    ans = 0
    ls = ['']
    temp = (data[cnt]).split(' ')
    n = int(temp[0])
    m = int(temp[1])
    for s in data[cnt + 1:cnt + n + 1]:
        ls += addd(s)
    cnt += n
    for s in data[cnt + 1:cnt + m + 1]:
        ans += check(s, ls)
    cnt += m
    print >>fout, 'Case #' + str(z) + ':', str(ans)
    cnt += 1
    z += 1
fin.close()
fout.close()