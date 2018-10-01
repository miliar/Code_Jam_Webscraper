import sys

fin = open(sys.argv[1],'rU')
fout = open(sys.argv[2],'w')
T = int(fin.readline().strip())

for case in xrange(T):
    print case, '...'
    R,k,N = map(int,fin.readline().split())
    g = map(int,fin.readline().split())
    ride = []
    for i in xrange(N):
        size, pos = 0, i
        while size+g[pos] <= k:
            size += g[pos]
            pos = (pos+1)%N
            if pos == i:
                break
        ride.append((size, pos, 1))
    
    rides = ride[:]
    for i in xrange(N):
        size, num_rides, seen, pos = 0, 0, [], i
        while pos not in seen:
            seen.append(pos)
            this = rides[pos]
            size += this[0]
            pos = this[1]
            num_rides += this[2]
        rides[i] = (size, pos, num_rides)
    
    money, pos, num_rides = 0, 0, 0
    while num_rides < R:
        if num_rides + rides[pos][2] > R:
            x = ride[pos]
            factor = 1
        else:
            x = rides[pos]
            if x[1] == pos:
                factor = (R - num_rides) / x[2]
            else:
                factor = 1
        money, pos, num_rides = money+(x[0]*factor), x[1], num_rides + (x[2]*factor)
    fout.write("Case #%i: %i\n" % (case+1, money))

fin.close()
fout.close()