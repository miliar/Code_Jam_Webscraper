file1 = open('input.txt')
file2 = open('output.txt','w')
a = int(file1.readline())
p = 1
while (a > 0):
    b = file1.readline()
    b1 = b.split()
    c = float(b1[0])
    f = float(b1[1])
    x = float(b1[2])
    rate = 2.0
    Tnext = 0.0
    Tprev = 0.0
    tnext = 0.0
    tprev = 0.0
    time = 0.0
    while (Tnext + tprev <= Tprev):
        time = time + tprev
        tprev = c/rate
        Tprev = x/rate
        rate = rate + f
        tnext = c/rate
        Tnext = x/rate
    time = time + Tprev
    file2.write("Case #%s: %s\n" % (p,time))
    p = p+1
    a = a-1
file2.close()
        
