import math
import random
import time
start_time = time.time()

f = open("A.txt",'r')
ntests = int(f.readline())

g = open("output.txt",'w')

def quicksort(L, M): #M sorted by L ordering
    ln = len(L)
    if ln<=1:
        return [L,M]

    lessL = []
    greaterL = []
    lessM = []
    greaterM = []

    r = random.randint(0,ln-1)
    t = L[r]

    equals = 0 #in case all equal

    for i in range(ln):

        s = L[i]
        if s<=t:
            lessL.append(s)
            lessM.append(M[i])
            if s==t:
                equals+=1
        else:
            greaterL.append(s)
            greaterM.append(M[i])

    if equals == ln:
        return [lessL,lessM]

    x = quicksort(lessL,lessM)
    y = quicksort(greaterL,greaterM)
    
    return [x[0]+y[0],
            x[1]+y[1]]


for i in range(ntests):
    p1 = f.readline()
    q1 = p1.split()

    N = int(q1[0])
    X = int(q1[1])




    p2 = f.readline()
    q2 = p2.split()

    ln = len(q2)

    for j in range(ln):
        q2[j] = int(q2[j])

    q2 = quicksort(q2,q2)[0]

    total = 0

    while len(q2)>0:
        if len(q2)==1:
            total+=1
            del q2[0]
        else:
            a = q2[-1]
            t = X-a
            if q2[0]>t:
                total+=1
                del q2[-1]
            else:
                total+=1
                del q2[-1]
                del q2[0]
    
        


            
        
        

    s = total

    g.write("Case #{}: {}\n".format(i+1,s))
    
f.close()
g.close()

print (time.time() - start_time, "secs")
