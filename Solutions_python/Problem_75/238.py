'''
Created on 2011/5/7

@author: bletchley
'''

filename = "../B-large.in"
file = open(filename)

TestN = int(file.readline())
TestCase = 0
item = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
while(TestCase < TestN):
    str = file.readline()
#    Q, W, E, R, A, S, D, F
    composeT = {}
    decompoT = {}
    for i in item :
        composeT[i]={}
        for j in item :
            composeT[i][j]=''
        decompoT[i]={}
        for j in item :
            decompoT[i][j]=False
    
    arr = str.split(' ')
    composeN = int(arr[0])
    decomN   = int(arr[composeN+1])
    total    = int(arr[composeN+decomN+2])   
    tra      = arr[composeN+decomN+3]  
#    print "compse : "
    for i in range(composeN):
        base = 1;
        list = arr[i+base]
#        print list
        composeT[list[0]][list[1]]=list[2]
        composeT[list[1]][list[0]]=list[2]
    
    for i in range(decomN):
        base = composeN+2;
        list = arr[i+base]
#        print list
        decompoT[list[0]][list[1]]=True
        decompoT[list[1]][list[0]]=True
    
#    print "number"
#    print composeN , decomN ,total   
#    if(TestCase==0) : composeT['Q']['W']='E'   
#    print 'W' in composeT['Q']    
#    print decompoT
#    print "travel"
    elementlist =[]
    for i in range(total):
#        print tra[i]
        if(len(elementlist)==0):
            elementlist.append(tra[i])
            continue
        if( elementlist[-1] in item and composeT[elementlist[-1]][tra[i]]!=''):
           elementlist[-1]=composeT[elementlist[-1]][tra[i]]
           continue;
        flag = False
        for thing in elementlist :
           if(thing in item and decompoT[thing][tra[i]]==True):
               elementlist=[] 
               flag=True
               break
        if(flag==False): elementlist.append(tra[i])   
        
    TestCase+=1;
#    ans=""
    
    ans= "Case #%d"%TestCase
#    print ,
    ans+=": ["
    firflag = False
    for e in elementlist :
        if(firflag): ans+=", "
        else : firflag = True
        ans+= e
    ans+="]"
    print ans
    
    


