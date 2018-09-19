import os

fi = open('C:\\Users\\VINSY\\Desktop\\30.in','r')
f2 = open('C:\\Users\\VINSY\\Desktop\\3.out','w')

T = int(fi.readline())

for i in range(1,T+1):
    lin = fi.readline()
    line = lin.split()
    A = int(line[0])
    B = int(line[1])
    count = 0
    done = {}
    digits = len(line[0])
    for j in range(A,B+1):
        flag=0
        done[j]=[]
        for k in range(1,digits):
            temps = str(j)[k:]+str(j)[:k]
            p = int(temps)
            if j < p and p>=A and p<=B and p not in done[j]:
                if p not in done:
                    count = count+1
                    done[j].append(p)
    b = "Case #"+str(i)+": "
    f2.write(b)
    f2.write(str(count))
    if i < T:
        f2.write('\n')

fi.close()
f2.close()

