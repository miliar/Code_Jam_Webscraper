# If we have n farms, the number of cookies produced at time t is:
# cookies(t,n) = V*t + (F*(t-t(1)) - C) + (F*(t-t(2)) - C) + ... + (F*(t-t(n)))
# with t(n) = t(n-1) + deltaT(n-1)
# with deltaT(k) = C / (V + k*F)
# If cookies(T,n) = X then
# T = (X + n*C + F*alpha(n)) / (V + n*F)
# with alpha(n) = n*deltaT(1) + (n-1)*deltaT(2) + ... + deltaT(n)

def f(n, V, C, F, X):
    return (X + n*C + F*alpha(n, C, V, F)) / (V + n*F)

def alpha(n, C, V, F):
    res = 0
    for i in range(1, n+1):
        res += i * deltaT(n-i, C, V, F)
    return res

def deltaT(k, C, V, F):
    return C / (V + k*F)

def parser(filename):
    f = open(filename, 'r')
    n = int(f.readline())
    res = []
    for i in range(n):
        s = f.readline()[:-1].split(' ')
        s = [float(k) for k in s]
        res.append(s)
    return res

from sys import argv
cnt = 0
for s in parser(argv[1]):
    cnt += 1
    buf = f(0, 2, s[0], s[1], s[2])
    farm = 1
    res = f(farm, 2, s[0], s[1], s[2])
    while res < buf:
        buf = res 
        farm += 1
        res = f(farm, 2, s[0], s[1], s[2])
    print 'Case #'+str(cnt)+': '+str(buf)
