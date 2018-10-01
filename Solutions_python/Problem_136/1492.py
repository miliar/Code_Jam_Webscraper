z = open('B-large.in', 'r')
w = open('OUT.txt','w')
n = int(z.readline())

for q in range (n):
    k = z.readline()
    a = k.strip().split()
    c = float(a[0])
    f = float(a[1])
    x = float(a[2])
    k = 0
    b = False
    t1 = x/2
    while (b == False):
        t2 = t1 + c/(2 + k*f) - x/(2 + k*f) + x/(2 + (k+1)*f)
        if t2 >= t1:
            break
        t1 = t2
        k +=1
    w.write('Case #' + str(q+1) + ": " + str(round(t1,7)) + "\n")
z.close()
w.close()