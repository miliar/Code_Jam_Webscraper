def search(x,lst):
	for a in lst:
		if a>x:
			return lst.index(a)
	return -98

def copy(lst):
	tmp=[]
	for x in lst:
		tmp.append(x)
	return tmp
'''DECITFUL WAR'''

g=open("txt","r")
cases=int(g.readline())
i=0
while(1):
    score=0
    score1=0
    n=int(g.readline())
    arr1=g.readline().split()
    naomi=[]
    ken=[]
    for x in range(n):
	       naomi.append(float(arr1[x]))
    
    arr2=g.readline().split()
    for x in range(n):
	       ken.append(float(arr2[x]))
     
    ken.sort()
    naomi.sort()
    ken1=copy(ken)
    naomi1=copy(naomi)
    	
    while(naomi!=[]):
	if(naomi[-1]>ken[-1]):
		score+=1
		naomi.pop(-1)
		ken.pop(-1)
    	
        else:
            min_n=naomi[0]
    	    max_k=ken[len(ken)-1] 
    	    if(len(ken)>1):
                    max_k1=ken[len(ken)-2]

            elif(len(ken)==1):
		    max_k1=max_k
    
    	    if(min_n<max_k):
          	    n_told=.5*(max_k+max_k1)
	    elif(min_n>max_k):
		    n_told=min_n
    	    if(n_told>max_k):
                score+=1
        
    	    naomi.pop(0)
    	    ken.pop(-1)
    print 'Case #'+str(i+1)+':',score,


    while(naomi1!=[]):
	 index=search(naomi1[0],ken1)
	 #print index,'INDEX'
	 if(index!=-98):
		 naomi1.pop(0)
		 ken1.pop(index)
         elif(index==-98):
		 score1+=1
		 naomi1.pop(0)
		


    i+=1
    print score1
    if(i==cases):
	       break


			
'''HONEST WAR'''
