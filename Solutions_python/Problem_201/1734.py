
import math

def readData(input_file):
    f=open(input_file)
    numCase=int(f.readline())
    #print numCase
    N  =[]
    K =[]
    for i in range(numCase):
        line = f.readline()
        #print line
        N.append(int(line.split()[0]))
        K.append(int(line.split()[1]))
    return numCase, N, K


def f(N,K):
    level = int(math.log(K) / math.log(2)) + 1
    div = 2**level
    i = (N - (div-1)) / div
    offset = K - 2**(level-1)
    rem = N - (div-1) - i * div
    L = (i+1) if offset < rem else i
    R = (i+1) if offset < (rem - div/2) else i
    return (L,R)
 
def stallProb(N,K):
    myArray=[N]
    for i in range(K):
        myArray=sorted(myArray)
        temp=(myArray[-1]-1)/2.0
        del(myArray[-1])
        if temp==int(temp):
            l = int(temp)
            r = int(temp)
            myArray.append(int(temp))
            myArray.append(int(temp))
        else:
            l = int(temp)
            r = int(temp)+1
            myArray.append(int(temp))
            myArray.append(int(temp)+1)
    return max(l,r),min(l,r)
        


input_file="C-small-2-attempt2.in"
numCase,N,K  = readData(input_file)
for i in range(numCase):
    ans = f(N[i],K[i])
    print 'Case #'+str(i+1)+': '+str(ans[0])+' '+str(ans[1])
