import numpy as np
file = open('C:\\Users\\V\\Downloads\\filefile.txt','r')
b = file.read()
file.close()    
data = b.split('\n')
n = int(data[0])
file = open('C:\\Users\\V\\Downloads\\Codejam.txt','w')
for i in range(n):
    dat = data[i + 1].split(" ")
    n = int(dat[0])
    k = int(dat[1])
    ar = np.zeros(n + 2)
    ar[0] = 1
    ar[n + 1] = 1
    ans = 0
    ans1 = 0
    m = 0
    for j in range(k):
        c = 1
        temp = 0
        mp = 0
        m = 0
        while c < n + 1:
            if ar[c] == 0:
                temp += 1
            else:
                temp = 0
            if temp > m:
                m = temp
                mp = c
            c += 1
        #print "max =", m
        #print mp - (m - 1) / 2
        ar[mp - (m - 1) / 2] = 1
        ans = (m) / 2
        ans1 = (m - 1) / 2
    #print ans, ans1
    file.write("Case #" + str((i + 1)) + ": "  + str(ans) + " " + str(ans1) + '\n')
file.close()