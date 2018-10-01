import math
def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("C-small-2-attempt0.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for ii in range(inpNum):
    qn = a[ii].split(" ")
    N = int(qn[0])
    K = int(qn[1])
    powerK = math.log(K+1, 2)
    powerK = int(math.ceil(powerK)) -1
    
    for i in range(0, powerK):
        K -= 2**i
    
    even = [-1,0]
    odd = [-1,0]
    if N%2 == 0:
        even=[N,1]
    else:
        odd=[N,1]
    for i in range(powerK):
        newE=[-1, 0]
        newO=[-1, 0]
        if even[0]!=-1:
            e = even[0]//2
            if e%2 == 0:
                newE = [e, even[1]]
                newO = [e-1, even[1]]
            else:
                newO = [e, even[1]]
                newE = [e-1, even[1]]
        if odd[0]!= -1:
            e = (odd[0]-1)/2
            if e%2 == 0:
                if even[0]!=-1:
                    newE[1] += odd[1]*2
                else:
                    newE = [e, odd[1]*2]
            else:
                if even[0]!=-1:
                    newO[1] += odd[1]*2
                else:
                    newO = [e, odd[1]*2]
        even = newE
        odd = newO
    if even[0]>odd[0]:
        oddn = int(even[0]/2)
        if K<=even[1]:
            ans = [oddn, oddn-1]
        else:
            ans = [oddn-1, oddn-1]
            
    else:
        oddn = int((odd[0]-1)/2)
        if K<=odd[1]:
            ans = [oddn, oddn]
        else:
            ans = [oddn, oddn-1]
    outp(ii, " ".join(map(str, ans)))







    
##    psudoBinary = []
##    for i in range(1, powerK):
##        K -= 2**i
##    for i in range(powerK-1, -1, -1):
##        if K >2**i:
##            psudoBinary.append(1)
##            K -= 2**i
##        else:
##            psudoBinary.append(0)
##    for i in range(powerK-1)
    

    
            
    
    
    
