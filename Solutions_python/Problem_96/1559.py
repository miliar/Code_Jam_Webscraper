'''
Created on 14-Apr-2012

@author: abhijit
'''

def find_most_optimal(ll,n,S):
    num=0
    surprising=0
    indices=[]
    for no in ll:
        if(no%3==0):
            maxval=no/3
        else:
            maxval=(no/3)+1
        if(maxval>=n):
            num+=1
            indices.append(ll.index(no))
    
    for i in range(len(ll)):
        if(not(indices.__contains__(i))):
            no=ll[i]%3
            gos=ll[i]/3
            if(no==2):
                maxval=gos+2
            else:
                maxval=gos+1
            if(maxval>=n and ll[i]!=0):
                surprising+=1
            if(ll[i]==0 and n==0):
                surprising+=1
    if(surprising>=S):
        num+=S
    else:
        num+=surprising
    return num
        
        


input_val=int(raw_input())
strings=[]




for i in range(input_val):
    string=raw_input()
    strings.append(string)
N=0
S=0
p=0
T=[]
case=1
for st in strings:
    T=[]
    params=st.split()
    N=int(params[0])
    S=int(params[1])
    p=int(params[2])
    for i in range(N):
        T.append(int(params[3+i]))
#    print T
    number=find_most_optimal(T,p,S)
    print "Case #"+str(case)+": "+str(number)
    case+=1
    