#!/usr/bin/python
##reading input file.....
fname=raw_input("input filename:")
data=open(fname,"r+")
text=data.readlines()
data.close()
nos=int(text[0])
nos=nos

def main(ln):
    
    check=0
    for x in range(0,4):
     xn=0
     on=0
     tn=0
     for y in range(0,4):
      if ln[x][y]=='X':
       xn+=1
      elif ln[x][y]=='O':
       on+=1
      elif ln[x][y]=='T':
       tn+=1

     if xn==4:
      return "X won"
      check+=1
      break
     if on==4:
      return "O won"
      check+=1
      break
     if xn==3 and tn==1:
      return "X won"
      check+=1
      break
     if on==3 and tn==1:
      return "O won"
      check+=1
      break

    for y in range(0,4):
     xn=0
     on=0
     tn=0
     for x in range(0,4):
      if ln[x][y]=='X':
       xn+=1
      elif ln[x][y]=='O':
       on+=1
      elif ln[x][y]=='T':
       tn+=1
     if xn==4:
      return "X won"
      check+=1
      break
     if on==4:
      return "O won"
      check+=1
      break
     if xn==3 and tn==1:
      return "X won"
      check+=1
      break
     if on==3 and tn==1:
      return "O won"
      check+=1
      break
    xn=0
    on=0
    tn=0
    for x in range(0,4):
     for y in range(0,4):
      if x==y:
       if ln[x][y]=='X':
        xn+=1
       elif ln[x][y]=='O':
        on+=1
       elif ln[x][y]=='T':
        tn+=1
    if xn==4:
      return "X won"
      check+=1
      
    if on==4:
      return "O won"
      check+=1
      
    if xn==3 and tn==1:
      return "X won"
      check+=1
      
    if on==3 and tn==1:
      return "O won"
      check+=1
      
    lis=[]
    lis.append(ln[0][3])
    lis.append(ln[1][2])
    lis.append(ln[2][1])
    lis.append(ln[3][0])   
    xn,tn,on=0,0,0
    for x in lis:
     
      
       if x=='X':
        xn+=1
       elif x=='O':
        on+=1
       elif x=='T':
        tn+=1
    if xn==4:
      return "X won"
      check+=1
      
    if on==4:
      return "O won"
      check+=1
      
    if xn==3 and tn==1:
      return "X won"
      check+=1
      
    if on==3 and tn==1:
      return "O won"
      check+=1
   
      

    if check==0:
     for x in range(0,4):
      for y in range(0,4):
       if ln[x][y]==".":
        return "Game has not completed"
        check=+1
        break
     if check==0:
       return "Draw"
    
##   For printing output...   
def fun(line1,line2,line3,line4,x):
    line1=line1.strip()
    line2=line2.strip()
    line3=line3.strip()
    line4=line4.strip()
    lin1=list(line1)
    lin2=list(line2)
    lin3=list(line3)
    lin4=list(line4)
    ln=[lin1,lin2,lin3,lin4]
    value=main(ln)
    out=open("out.txt","a+")
    out.writelines("case #%d: %s \n" %(x,value))     
    out.close()
   
for x in range(0,nos):
    line1=text[4*x+1+x]
    line2=text[4*x+2+x]
    line3=text[4*x+3+x]
    line4=text[4*x+4+x]
    fun(line1,line2,line3,line4,x+1)

print "Result is stored in out.txt file successfully!!"
