import sys
def solve(D,horses):
    speed =-1
    for h in horses:
        if speed != -1 and h['speed'] > speed:
            continue
        time_to_arrive = (D-h['distance'])/h['speed']
        new_speed = D/time_to_arrive
        if speed != -1 and new_speed > speed:
            continue
        speed = new_speed

    return speed
#fin=open('A-small-attempt1.in')
#fin = open('sample.in')
fin = sys.stdin
T = int(fin.readline())
for t in xrange(T):
    D,N = (int(t) for t in fin.readline().split(' '))
    horses = []
    for n in xrange(N):
        ki,si = (float(s) for s in fin.readline().split(' '))
        horses.append({'distance':ki,'speed':si})

    speed= solve(D,horses)
    print("Case #%d: %f"%(t+1, round(speed,6)))

fin.close()