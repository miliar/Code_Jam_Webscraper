#-*- coding:utf-8 -*-

import string

def computeMin(c,f,x):
    cookiePre =2
    minTime =0
    cookieNow = cookiePre + f
    t1 = x/cookiePre
    t2 = c/cookiePre+x/cookieNow
    while 1:
        if t1 < t2:
            minTime += t1
            break
        else:
            minTime += c/cookiePre
            cookiePre +=f
            cookieNow +=f
            t1 = x/cookiePre
            t2 = c/cookiePre + x/cookieNow
    #print minTime
    return minTime
        
    


f=open(r'F:B-large.in')
fw=open(r'F:\B-large.out','w')
caseNum=string.atoi(f.readline()) 



  
#测试caseNum个case
for i in range(caseNum): 
    numList = f.readline().strip().split()
    C = string.atof(numList[0])
    F = string.atof(numList[1])
    X = string.atof(numList[2])
    
    fw.write('Case #%d: %.7f\n' %(i+1,computeMin(C,F,X)))
    
   
    
f.close()
fw.close()