
# coding: utf-8

# In[133]:

#mode = 'practice'
#mode = 'small'
mode = 'large'
problem = 'A'
attempt = '0'


# In[134]:

import numpy as np
if mode == 'practice':
    infile = 'input.txt'
    outfile = 'output.txt'
if mode == 'small':
    infile = problem+'-small-attempt'+attempt+'.in'
    outfile = problem+'-small.out'
if mode == 'large':
    infile = problem+'-large.in'
    outfile = problem+'-large.out'
f = open(infile, 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
outputfile = open(outfile, 'w')
pos = 0


# In[135]:

def order(N,R,H):
    indices = sorted(enumerate(R), key=lambda x:x[1])
    oR = []
    oH = []
    for i in range(len(indices)):
        oR.append(R[indices[i][0]])
        oH.append(H[indices[i][0]])
    oR.reverse()
    oH.reverse()
    return oR,oH


# In[136]:

def findBest(N,oR,oH):
    best = 0
    pen = oR[0]*oR[0]-oR[1]*oR[1]+2*oR[0]*oH[0]
    for i in range(N-1):
        area =  2*oR[i+1]*oH[i+1]
        if area < pen:
            best = i+1
            pen = area
    return best


# In[137]:

def solve(N,K,R,H):
    oR, oH = order(N,R,H)
    while N > K:
        remove = findBest(N,oR,oH)
        del oR[remove]
        del oH[remove]
        N=N-1
    area = oR[0]*oR[0]
    for i in range(N):
        area = area + 2*oR[i]*oH[i]
    return area * np.pi


# In[138]:

for i in range(cases):
    pos=pos+1
    R = []
    H = []
    nums = lines[pos].rstrip().split(" ")
    N = int(nums[0])
    K = int(nums[1])
    for j in range(N):
        pos=pos+1
        nums = lines[pos].rstrip().split(" ")
        R.append(int(nums[0]))
        H.append(int(nums[1]))
    out = "CASE #" + str(i+1) + ": " + str(solve(N,K,R,H))
    outputfile.write(out)
    outputfile.write("\n")


# In[139]:

outputfile.close()


# In[ ]:



