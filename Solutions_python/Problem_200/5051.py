# -*- coding: utf-8 -*-
a=open("C:\\GoogleCodeJam\\tidyNumbers\\\\B-small.in",'r')

b=a.read()
lines=b.split("\n")

tests=[]

  

class Test:
    def __init__(self,line):
        self.line=line
        
    def traite(self):
        return str(lastTidy(int(self.line)))


def isTidy(num):
    s=str(num)
    num2=''.join([str(a) for a in (sorted([int(e) for e in s]))])
    return num==int(num2)

def lastTidy(num):
    for i in range(num,-1,-1):
        if isTidy(i):
            return i
    return None    


        
            

N=int(lines[0])
i=1
for a0 in range(N):
   line=lines[i]
   tests.append(Test(line))
   i+=1
        
a.close()    


                            


c=open("C:\\GoogleCodeJam\\tidyNumbers\\output.txt",'w')    

for i in range(len(tests)):
    c.write("Case #"+str(i+1)+": "+(tests[i].traite()+"\n")) 
    print("Case #"+str(i+1)+": "+(tests[i].traite()+"\n"))  
c.close()                         
