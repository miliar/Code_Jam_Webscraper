'''
Created on Apr 8, 2017

@author: morettini
'''
import heapq
from lxml.html.builder import BIG

def main():
    input=open('input.txt', 'r')
    output=open('output.txt', 'w')
    Tcases=input.readline()
    currentCase=0
    heap=[]
    mlist=[]
    
    for i in range (0,1000000):
        if(2**i >1000000):
            break
        mlist.append(2**i)
        
    for line in input:
        
        
        currentCase=currentCase+1
        if(currentCase==13):
            pass
        par=line.split(' ')
        N=int(par[0])
        K=int(par[1])
        
        #N=N-(K-1)
        
        j=len(mlist)-1
        while(K-1<mlist[j]-1):
            j=j-1
        N=N-(mlist[j]-1)
        #dimensione spazi
        spaces=float(N)/mlist[j]
        if(spaces%1 !=0 ):
            dim1= spaces-(spaces%1)
            dim2=dim1+1
            #ydim2--->dim2
            ydim2=(N-mlist[j]*dim1)/(dim2-dim1)
            #xdim1--->dim1
            xdim1=mlist[j]-ydim2
            if(dim1>dim2):
                big=dim1
                small=dim2
                xBIG=xdim1
                xSMALL=ydim2
            else:
                big=dim2
                small=dim1
                xBIG=ydim2
                xSMALL=xdim1 
            K=K-(mlist[j]-1)
            K=K-xBIG 
            if(K<=0):
                if (big % 2 == 0): #even 
                    max=big/2
                    min=max-1
                else: #odd
                    max=big/2
                    min=big/2
            else:
                if (small % 2 == 0): #even 
                    max=small/2
                    min=max-1
                else: #odd
                    max=small/2
                    min=small/2
        else:
            if (spaces % 2 == 0): #even 
                max=spaces/2
                min=max-1
            else: #odd
                max=spaces/2
                min=spaces/2
            
        #=======================================================================
        # for k in range (1,K):
        #     larger=heap.pop(0)-1
        #     if (larger % 2 == 0): #even 
        #         heap.append(larger/2)
        #         heap.append(larger/2)
        #     else: #odd
        #         heap.append((larger+1)/2)
        #         heap.append((larger-1)/2)
        #     heapq._heapify_max(heap)
        #     
        # larger=heap.pop(0)-1
        # max=0
        # min=0
        # if (larger % 2 == 0): #even 
        #     max=larger/2
        #     min=larger/2
        # else: #odd
        #     max=(larger+1)/2
        #     min=(larger-1)/2 
        #=======================================================================
        if(min<0):
            min=0
        output.write("Case #"+ str(currentCase)+": "+ str(int(max))+" "+str(int(min))+"\n") 
   
    #output.flush()
    output.close()
    
if __name__ == '__main__':
    main()