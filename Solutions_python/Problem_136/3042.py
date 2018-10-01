import numpy as np
fi = open("ccin.txt", 'r')
fo = open("ccout.txt",'w+')
inp = fi.read()
inp = inp.split('\n')
T = int(inp[0])
B = 2.0
for i in range(T):
    d = np.array(inp[i+1].split()).astype(float)
    C, F, X = d
    z = int(X/C)+1
    if z < 5:
        z = 5
    tx = X/(np.ones(z)*B + np.arange(z)*F)
    tc = np.hstack((np.zeros((1)),C/(np.ones(z-1)*B + np.arange(z-1)*F)))
    for j in range(1,z):
        tc[j] += tc[j-1]
    fo.write("Case #%d: %f\n" % ((i+1), np.min(tc+tx)))

fi.close()
fo.close()


