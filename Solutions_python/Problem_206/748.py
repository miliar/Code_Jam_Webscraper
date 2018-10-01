filein = open('A-large.in', 'r')
fileout = open('A-large.out', 'w')
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    [D, N] = [int(x) for x in filein.readline().split()]
    ks = []
    for i in range(N):
        ks.append([int(x) for x in filein.readline().split()])
    time = 0
    for i in range(N):
        k, s = ks[i]
        time = max(float(D - k)/s, time)
    speed = D / time
    fileout.write(str(speed) + '\n')

filein.close()
fileout.close()