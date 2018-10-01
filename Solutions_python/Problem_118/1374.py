import math
fname=raw_input("input filename:")
data=open(fname,"r+")
text=data.readlines()
data.close()
nos=int(text[0])
nos=nos
tn=1

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def reve(num):
    r=0
    while(num>0):
     dig=num%10
     r=r*10+dig
     num=num/10
    return r
 
def fun(A,B,c):
    count=0
    for x in xrange(A,B+1):
      if is_square(x):
       h=reve(x)
       if h==x:
         z=int(math.sqrt(h))
         q=reve(z)
         if q==z:
          print q
          count+=1
    value=count
    out=open("out.txt","a+")
    out.writelines("Case #%d: %d \n" %(c,value))     
    out.close()
   
for x in range(0,nos):
    ln=text[x+1]
    ln=ln.strip()
    ln1=ln.split()
    A=int(ln1[0])
    B=int(ln1[1])
    fun(A,B,x+1)
    

