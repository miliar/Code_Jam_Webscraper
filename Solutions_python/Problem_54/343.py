def GCD(x,y):
    while y != 0:
        (x, y) = (y, x%y)
    return x

def create_subtractions(a):
    ans = []
    for x in xrange(len(a) - 1):
        for y in xrange(x + 1, len(a)):
            ans += [abs(a[x] - a[y])]
    return ans

fin = open('small.in')
fout = open('small.out', 'w')
data = fin.readlines()
for x in xrange(len(data)):
    data[x] = (data[x])[:-1]
t = int(data[0])

for x in xrange(1, t + 1):
    times = []
    differents = []
    temp = (data[x]).split(' ')
    tp = len(temp)
    i = 1
    while i < tp:
        times += [int(temp[-i])]
        i += 1
    differents = create_subtractions(times)
    for y in xrange(1, len(differents)):
        differents[y] = GCD(differents[y], differents[y-1])
    ans = times[0] % differents[-1]
    if ans != 0:
        ans = differents[-1] - ans
    print >>fout, 'Case #' + str(x) + ':', str(ans)

fout.close()
fin.close()