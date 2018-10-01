f = open('C:\Users\Brijesh\Desktop\A-small-attempt2.in','r');
file =[]
file = f.readlines();
tc = int(file[0])
r=1
line = 1
while(r<=tc):
    ans1 = int(file[line])-1
   
    line +=1
    mat1 = [] 
    mat2 = [] 
    for i in range(4):
        element = file[line]
        line +=1
        mat1.append(element.split())
    
    
    new_mat1 = [[],[],[],[]]
    new_mat2 = [[],[],[],[]]     
    k = 0
    for i in mat1:
        for j in i:    
            new_mat1[k].append(int(j))            
        k+=1   
    
    
    ## matrix 2    
    ans2 = int(file[line])-1
    line+=1
    for i in range(4):
        element = file[line]
        line+=1  
        mat2.append(element.split())

       
    k = 0   
    for i in mat2:
        
        for j in i:
            new_mat2[k].append(int(j))            
        k+=1
    
    
    ##finding the solution
    count =0
    flag =0
    for i in new_mat1[ans1]:
        if i in new_mat2[ans2]:
            res = i
            count += 1
        else:
            flag =1
    
    if(count>1):
        print "Case #"+str(r)+": Bad magician!"
    
    elif(count == 1):
        print "Case #"+str(r)+": "+str(res)
        
    elif(flag == 1):
        print "Case #"+str(r)+": Volunteer cheated!"  
          
    r+=1     
