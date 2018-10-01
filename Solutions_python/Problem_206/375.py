n = int(raw_input())

#def compute(horses, i):
#    pass

for i in xrange(n):
    D, N = map(int, raw_input().split(' '))
    horses = []
    for j in xrange(N):
        K, S = map(int, raw_input().split(' '))
        horses.append((D-K, S, float(D-K)/S))
    # sorted horses in distance from destination
    #horses.sort()
    #for j in xrange(len(horses)):
    #    compute(horses, j)
    horses.sort(key=lambda x: x[2])
    speed = round(D/horses[-1][2], 6)
    print 'Case #' +str(i+1) + ': ' + str(speed)

