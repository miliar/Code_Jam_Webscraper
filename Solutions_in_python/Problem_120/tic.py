#!/usr/bin/python
##reading input file.....
fname=raw_input("input filename:")
data=open(fname,"r+")
text=data.readlines()
data.close()
nos=int(text[0])


def main(r,t):
    su=0
    count=0
    while su<=t:
     z=2*r+1
     r=r+2
     su=su+z
     count+=1
    return count-1
    
##   For printing output...   
def fun(line,x):
    line=line.strip()
    ln=line.split()
    
    r,t=int(ln[0]),int(ln[1])
    value=main(r,t)
    out=open("out.txt","a+")
    out.writelines("Case #%d: %d \n" %(x,value))     
    out.close()
   
for x in range(1,nos+1):
    line=text[x]
    fun(line,x)

print "Result is stored in out.txt file successfully!!"
