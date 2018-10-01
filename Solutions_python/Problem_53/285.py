f = open("data.txt")
g = open("data1.txt", 'w')
j = int(f.readline())
for i in range(1, j+1):
    h = f.readline()
    h = h.partition(' ')
    n = int(h[0])
    k = int(h[-1])
    u = k % (2**n)
    if u == (2**n)-1:
        l = 'ON'
    else:
        l = 'OFF'
    string = 'Case #'+str(i)+": "+l+'\n'
    g.write(string)
