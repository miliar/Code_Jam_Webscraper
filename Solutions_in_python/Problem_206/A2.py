import sys
import math


def calcSpeed(D, d, s):
    return D*s/(D-d)

def calcSpeed2(D, d2, s2, tb):
    return D*s2/(s2*tb - d2 +1)

def catchupLoc(d1, s1, d2, s2):
    return (d1*s2 - d2*s1)/(s2 - s1)

def catchup(d1, s1, d2, s2):
    distance = d2-d1
    speed = s1-s2
    time = distance/speed
    location = s1*time + d1
    return location, time

T = int(sys.stdin.readline().strip())
for t in range(T):
    D, N = [int(i) for i in sys.stdin.readline().strip().split()]
    horses = []
    for i in range(N):
        horses.append([int(i) for i in sys.stdin.readline().strip().split()])

    horses.sort()
    speed = calcSpeed(D, horses[0][0], horses[0][1])
    newHorses = [horses[0]]
    for i in range(N-1):
        d1, s1 = horses[i]
        d2, s2 = horses[i+1]
        if s1 <= s2:
            break # horse never catches up
        tb = (d2-d1)/(s1-s2)
        lc = s1*tb + d1
        te = (D - lc)/s2 + tb
        S = D/te
        speed = min(speed, S)
    print('Case #{}: {:.6f}'.format(t+1, round(speed, 6)))
