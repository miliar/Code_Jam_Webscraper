import math
def myzip(plist):
    tmp = [[] for x in plist[0]]
    for i in range(len(plist)):
        for j in range(len(plist[i])):
            tmp[j].append(plist[i][j])

    return tmp

def get_distance(plist):
    xyz = myzip(plist)
    n = len(plist)
    x = 1.0*sum(xyz[0])/n
    y = 1.0*sum(xyz[1])/n
    z = 1.0*sum(xyz[2])/n
    dx = 1.0*sum(xyz[3])/n
    dy = 1.0*sum(xyz[4])/n
    dz = 1.0*sum(xyz[5])/n

    return ((dx**2+dy**2+dz**2),(2*(x*dx+y*dy+z*dz)),(x**2+y**2+z**2))


def get_min(m):
    print m
    A = 2*m[0]
    B = m[1]

    if A == 0:
        return 0
    else:
        return -1.0*B/A

def return_min(plist):
    m = get_distance(plist)
    t = get_min(m)
    if t < 0:
        dmin = math.sqrt(m[2])
        return dmin,0.0
    else:
        tmp = (t**2)*m[0]+t*m[1]+m[2]
        if tmp < 1e-10:
            tmp = 0
        dmin = math.sqrt(tmp)
        return dmin,t*1.0
