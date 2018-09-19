fn = "B-small-attempt0"
input = open(fn + ".in")
output = open (fn + ".out", "w")

def dist(x, y, z):
    from math import sqrt
    return sqrt(x*x + y*y + z*z)

def min(l, s):
    return - l / (2*s)
    

for case in range(1, int(input.readline())+1):
    f = int(input.readline())
    s=[0,0,0]
    v=[0,0,0]
    for n in range(f):
       h = input.readline().split()
       s[0]+=float(h[0]) / f
       s[1]+=float(h[1]) / f
       s[2]+=float(h[2]) / f
       v[0]+=float(h[3]) / f
       v[1]+=float(h[4]) / f
       v[2]+=float(h[5]) / f
    
    if v[0]==0 and v[1]==0 and v[2]==0:
        t = 0
    else:
        t = min(2 * (s[0]*v[0] + s[1]*v[1] + s[2]*v[2]), v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
        if t < 0 : t = 0
    d = dist(s[0]+v[0]*t, s[1]+v[1]*t, s[2]+v[2]*t)
    output.write("Case #" + str(case) + ": " + ("%.8f %.8f\n" % (d, t)))