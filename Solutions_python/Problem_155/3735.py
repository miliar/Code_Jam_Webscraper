result=""
theopen= open("ayman.in", "r")

theoutput=open("result.out", "w")

opens=open("output (1).out", "r")
print opens.read()
string=theopen.read()
from string import *
n=1
string=string.splitlines()
print string[55]
for line in string[1::]:
    #print line
    result+="Case #%d: "%n
    n+=1
    
    maxi=int(line[0])
    #print maxi
    #print "space"+line[1]
    x=int(line[2])
    for i in range(3,len(line)-1):
            
            #print i
            if x>=i-2:    
                x+=int(line[i])
            
                
    # x is the number of standing people, in a perfect word i'd just say maxi-x, but no, we were born to suffer
                
    for my in range(len(line)-2,1,-1):
            #print line[my], "my"
            #print my, "this is it"
            
                more=int(line[my])
                for j in range(my-1,1,-1):
                #print j, "hi"
                #print line[j]
                    more+=int(line[j])
                
            #print (my-2)-x+more, "ff",my-2
                
            if (my-2)-x>0:
                if (my-2)-x+more==maxi:
                    maxi=my-2
                    result+=str(maxi)+"maxi"



    if (maxi-x)>0: 
        result+= str(maxi-x)
    else: result+=str(0)    
    
    result+="\n"    
    #print "loop"    
    
    
print result        
theoutput.write(result)
theoutput.close()
