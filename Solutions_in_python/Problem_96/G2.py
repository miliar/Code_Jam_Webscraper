import os

fi = open('C:\\Users\\VINSY\\Desktop\\23.in','r')
f2 = open('C:\\Users\\VINSY\\Desktop\\2.out','w')

T = int(fi.readline())

for i in range(1,T+1):
    lin = fi.readline()
    line = lin.split()
    N = int(line[0])
    S = int(line[1])
    P = int(line[2])
    count = 0
    for j in range(3,N+3):
        k = int(line[j])
        if P >= 2:            
            if k >= (P*3-2):
                count = count+1
            elif k >= (P*3-4) and S > 0:
                count = count+1
                S = S-1
        else:
            if k >= (P*3-2):
                count = count+1
    b = "Case #"+str(i)+": "
    f2.write(b)
    f2.write(str(count))
    if i < T:
        f2.write('\n')

fi.close()
f2.close()

