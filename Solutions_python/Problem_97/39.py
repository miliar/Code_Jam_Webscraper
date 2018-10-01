def shift(num,l,i):
    n = (num % (10 ** (l-i))) * (10 ** i) + num / (10 ** (l-i))
    return n
def count(num,b):
    n = num
    l = 0
    rtv = 0
    while n > 0:
        n = n/10
        l += 1
    if l == 1:
        return 0
    else:
        buf = []
        for j in range(1,l):
            t = shift(num,l,j)
            if t > num and t <= b and (not t in buf):
                rtv += 1
                buf.append(t)
        return rtv       
fin = open('C-large.in','r')
fout = open('output.out','w')
T = eval(fin.readline())
for i in range(T):
    tmp = fin.readline()
    data = tmp.split()
    a = eval(data[0])
    b = eval(data[1])
    total = 0
    for num in range(a,b):
        total += count(num,b)    
    print >> fout,"Case #%d: %d" %(i+1,total)
fin.close()
fout.close()
