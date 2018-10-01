fh = open("a.in",'r')
fhw = open("b.txt",'w')
f = fh.readlines()
x = int(f[0].strip())
y1 = f[1:]
d = {}
l = 1
for t in y1:
    y = t.strip().split()
    N = int(y[0])
    S = int(y[1])
    p = int(y[2])
    s = 0
    n = 0
    for i in range(0,N):
        if p != 1:
            if int(y[(i + 3)]) > (3*p - 3):
                n = n + 1
            elif (int(y[(i + 3)]) == (3*p - 3)) or (int(y[(i + 3)]) == (3*p - 4)):
                if s < S:
                    n = n + 1
                s = s + 1
        else:
            if int(y[(i + 3)]) > 0:
                n = n + 1
    d[l] = "Case #" + str(l) +": " + str(n)
    l = l + 1
for p in range(1,x):
    fhw.write(d[p] + "\n")
fhw.write(d[x])
fh.close()
fhw.close()
