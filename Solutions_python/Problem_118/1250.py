from math import sqrt,floor
import copy
def check(lo):
    root = sqrt(lo)
    if floor(root)==root:
        root=int(root)
        if(check_pali(lo)):
            if(check_pali(root)):
                return True
    return False
    
    
    
def check_pali(num):
    num = str(num)
    #num=num.replace("\n","")
    num_list = list(num)
    
    rev=copy.deepcopy(num_list)
    rev.reverse()
    
    
    for i in range (0,len(num_list)):
        if int(num_list[i])!=int(rev[i]):
            return False
    return True
f=open("C-small-attempt0.in")
n = int(f.readline())
list_t = []
f2 = open("output.txt","w+")
for i in range (0,n):
    count=0 
    temp = f.readline()
    temp=temp.replace("\n","")
    arr = temp.split(" ")
    low = int(arr[0])
    up = int(arr[1])
  
    while low<=up:
        
        if(check(low)):
            count=count+1
        
        low=low+1
    out = "Case #"+str(i+1)+": "+str(count)+"\n"
    f2.write(out)
f2.close()



