import numpy as np
import sys
import itertools

f=open('B-small-attempt0.in', 'r')
f2=open('tidy_output.ou', 'w')

init=0
case=1
aliii=int(f.readline())

while case <= aliii:
    b=f.readline()
    #print b
    num=int(b)
    #print b.split('\n')
    num_list=np.array(list(b.split('\n')[0]))
    
    print num
    num_list=num_list.astype(int)
    
    prev_value=9
    answer=0
    shit=0
    answer=[]
    
    num_flip= num_list[::-1]
    neg=0
    
    for (i,aux) in enumerate(num_flip):
        flag=0
        aux2=aux+neg
        for aux3 in range(i+1,len(num_flip)):
            if sum(num_flip[aux3:]>num_flip[aux3-1]+neg)!=0:
                flag=1
        
        if flag==1:
            answer.append(9)
            neg=-1
        else:
            answer.append(aux2)
            neg=0
    
    result=0
    #print answer
    for aux in range(len(answer)-1,-1,-1):
        #print answer[aux]
        #print aux
        #print "------"
        result=answer[aux]*10**(aux)+result
    
    #if 10**len(str(result))-1<num:
    #    print "warning"
    #    result=10**len(str(result))-1
        
    print result
    print "-----------"
    f2.write('Case #')
    f2.write(str(case))
    f2.write(': ')
    f2.write(str(result))
    f2.write('\n')

    case+=1