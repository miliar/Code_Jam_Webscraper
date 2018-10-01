for I in range(int(input())):
    N = [int(n) for n in input()]


    if len(N)<2:
        print("Case #"+str(I+1)+": "+ "".join([str(c) for c in N]))
    
    else:
        i=0
        while i < len(N)-1 and N[i]<=N[i+1]:
            i+=1

        if i == len(N)-1:
            print("Case #"+str(I+1)+": "+ "".join([str(c) for c in N]))
        else:
            N[i]=N[i]-1
            j=i
            while j>0 and N[j-1]>N[j]:
                N[j-1]-=1
                N[j]=9
                j-=1
            for k in range(i+1, len(N)):
                N[k]=9

            if N[j]==0:
                print("Case #"+str(I+1)+": "+ "".join([str(c) for c in N[1:]]))
            else:
                print("Case #"+str(I+1)+": "+ "".join([str(c) for c in N]))



        
    
    
    


