
def isSubStr(w,b):
    #print w
    #print b
    if(len(w)==0):
        return 1
    else:
        if(len(b)==0):
            
            return 0
        if (w[0]==b[0]):
            
            tf=isSubStr(w[1:],b[1:])
            wf=isSubStr(w,b[1:])
            return tf+wf
        else:
            return isSubStr(w,b[1:])
            
                
FileIn=open("C-small-attempt2.in","r")

content=FileIn.read()

content=content.split('\n')





matchStr='welcome to code jam'

caseCounter=int(content[0])
print content[0]
#print content
i=0
FileOut=open('result2.out','w')

while i<caseCounter:
    
    #print content[i+1]
    #print isSubStr(matchStr,content[i+1])
    result=isSubStr(matchStr,content[i+1])
    result=str(result)
    if len(result)>4:
        result=result[(len(result)-4):]
    else:
        result=result.rjust(4,'0')
    FileOut.write("Case #"+str(i+1)+": "+result+'\n')
    i=i+1
    
    
FileOut.close()



    


    
