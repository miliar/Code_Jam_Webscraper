def war(list1,list2):
    score=0
    while(len(list1)!=0 and len(list2)!=0):
        if(max(list1)<max(list2)):
            list1.remove(max(list1))
            list2.remove(max(list2))
        elif(max(list1)>max(list2)):
            list1.remove(max(list1))
            list2.remove(min(list2))
            score=score+1
    return score
def dwar(list1,list2):
    score=0
    while(len(list1)!=0 and len(list2)!=0):
        if(min(list1)<min(list2)):
            list2.remove(max(list2))
            list1.remove(min(list1))
        elif(min(list1)>min(list2)):
            list1.remove(min(list1))
            list2.remove(min(list2))
            score=score+1
    return score
file=open('D-large.in','r')
cases=int(file.readline())
for case in range(1,cases+1):
    n=int(file.readline())
    list1=file.readline()
    list1=list1.split()
    list2=file.readline()
    list2=list2.split()
    listn1=list1[:]
    listn2=list2[:]
    print('Case #'+str(case)+': '+str(dwar(list1,list2))+' '+str(war(listn1,listn2)))
