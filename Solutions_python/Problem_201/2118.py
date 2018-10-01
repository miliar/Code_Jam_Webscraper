file = open("c:/CodeJam/2017/Qualifier/C-small-2-attempt1.in")
line = file.readline()

def bathroomstaller(openstalls):
    if openstalls%2==0:
        return [int(openstalls/2-1),int(openstalls/2)]
    elif openstalls%2==1:
        return [int((openstalls-1)/2),int((openstalls-1)/2)]
    
        

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    [n,k] = file.readline().split()
    # N = Number of Bathroom Stalls Initially Available
    N=int(n)
    #print('N= '+n)
    # K = Number of People Entering Bathroom In an Orderly Fashion
    K=int(k)
    #print('K= '+k)
    # List of Open Stalls in Open Blocks
    listofstalls={}

    listofstalls[N]=1
    
    while K>0:
        largeststallblock=max(listofstalls.keys())
        Nlargeststallblock=listofstalls[max(listofstalls.keys())]
        
        [Ls,Rs]=bathroomstaller(largeststallblock)

        if Ls in listofstalls:
            listofstalls[Ls]+=Nlargeststallblock
        else:
            listofstalls[Ls]=Nlargeststallblock

        if Rs in listofstalls:
            listofstalls[Rs]+=Nlargeststallblock
        else:
            listofstalls[Rs]=Nlargeststallblock

        del listofstalls[largeststallblock]
        K-=Nlargeststallblock
        

    print('Case #{}: {} {}'.format(testcase+1,str(Rs),str(Ls)))
           
file.close() 
        
        
    

    
    

