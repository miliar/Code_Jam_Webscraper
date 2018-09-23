import numpy as np
infile = open('in.txt')
outfile = open('out.txt','w')
T = int(infile.readline())
for cases in range(T):
    ss = infile.readline()
    lst = ss.split()
    ans = 0
    boo = True
    K = int(lst[1])
    s = lst[0]
    l = len(s)
    f = np.zeros([1,l + K])
    for i in range(l):
        if (s[i] == '-'):
            f[0, i] = f[0, i] != 1
        if (f[0, i] == 1):
            ans += 1
            for j in range (i, i+K):
                if (j>=l):
                    boo = False
                f[0, j] = f[0, j] != 1
    if (boo):
        ansString = "Case #"+str(cases+1)+": "+str(ans)+'\n'
        outfile.write(ansString)
    else:
        ansString = "Case #"+str(cases+1)+": IMPOSSIBLE\n"
        outfile.write(ansString)
infile.close()
outfile.close()