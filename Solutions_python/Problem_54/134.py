
def gcd(a, b):
    if a < b:
        t = a;
        a = b;
        b = t;
   # print a, b
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)


fin=open("1.in")
fout = open("2.out", 'w')
line = fin.read()
fin.close();
data = line.split()
icase = 1
tcase = int(data[0])
index = 1
while icase <= tcase:
    n = int(data[index])
    i = 0
    t=[]
    t = data[index + 1:index+n+1]
    i = 1
    while i < n:
        t[i] = int(t[i]) - int(t[0])
        if t[i] < 0:
            t[i] = t[i] * -1
        i = i + 1
    t[0] = int(t[0])
    cm = int(t[1])
    i = 2
    while i < n:
        cm = gcd(cm, int(t[i]))
        i = i + 1
    res = int(int(t[0])/cm)*cm
    if res < t[0]:
        res = res + cm
    res = res - int(t[0])
    str = "Case #%d: %d\n" %(icase, res)
    fout.write(str)
    icase = icase + 1
    index = index + int(data[index]) + 1

