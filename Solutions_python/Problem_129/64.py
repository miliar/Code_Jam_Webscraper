import math
import time
start_time = time.time()

f=open("A.txt",'r')
ntests = int(f.readline())

g = open("output.txt",'w')

for i in range(ntests):
    p = f.readline()
    p = p.split()

    N = int(p[0]) #stops: 0-N-1
    M = int(p[1])

    pairs = [] #store (in, out, #)

    for j in range(M):
        p = f.readline()
        p = p.split()
        pairs.append([int(p[0]),int(p[1]),int(p[2])])

    #sort by origin

    iS = 1
    while iS<M:
        non = pairs[iS]
        jS = iS
        while jS>=1:
            if pairs[jS][0]<pairs[jS-1][0]:
                a = pairs[jS]
                pairs[jS] = pairs[jS-1]
                pairs[jS-1] = a
            else:
                break
            jS-=1
        iS+=1

    s = 0 #sum

    while len(pairs)>1:

        k=1
        while k<len(pairs) and pairs[0][1]>=pairs[k][0]:
            if pairs[0][1]<pairs[k][1]:
                m = pairs[0][2]
                n = pairs[k][2]

                s += min(m,n)*(pairs[k][0]-pairs[0][0])*(pairs[k][1]-pairs[0][1])
                s %= 1000002013

                e2 = pairs[k][1]
                e1 = pairs[0][1]
                
                if m>n:
                    pairs[k][1] = e1
                    pairs[0][1] = e2
                    pairs[0][2] = n
                    pairs.insert(1,[pairs[0][0],e1,m-n])
                if m==n:
                    pairs[k][1] = e1
                    pairs[0][1] = e2
                if m<n:
                    pairs[0][1] = e2
                    pairs[k][1] = e1
                    pairs[k][2] = m
                    pairs.insert(k+1,[pairs[k][0],e2,n-m])
        
            k+=1
        del pairs[0]
    
                             
    
        
    g.write("Case #{}: {}\n".format(i+1,s))

    if i%1000==0:
        print(i)



    
f.close()
g.close()

print (time.time() - start_time, "secs")
