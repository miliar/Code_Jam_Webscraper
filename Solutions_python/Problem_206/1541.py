x='/storage/emulated/0/qpython/projects3/cj17r1b/'
with open(x+'a2.in','r') as f:
    with open(x+'a2.out','w') as o:
        T=int(f.readline().strip())
        for case in range(1,T+1):
            t = f.readline().strip().split(' ')
            D = int(t[0])
            N = int(t[1])
            horses = []
            for n in range(N):
                t = f.readline().strip().split(' ')
                horses.append([int(t[0]),int(t[1])])
            times = []
            for h in horses:
                times.append((D-h[0])/h[1])
            mytime = max(times)
            myspeed = D/mytime
            o.write('Case #{}: {}\n'.format(case,myspeed))
