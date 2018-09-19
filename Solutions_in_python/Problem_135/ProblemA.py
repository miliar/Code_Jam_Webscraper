def grid(n,a,b,c,d):
    if n=="1":
        return a
    if n=="2":
        return b
    if n=="3":
        return c
    if n=="4":
        return d


def ch1(s1,s2):
    c=[]
    for a in s1:
        for b in s2:
            if a==b:
                c.append(a)
    return c

def result(c):
    if len(c)==0:
        return "Volunteer cheated!"
    elif len(c)==1:
        return c[0]
    elif len(c)>1:
        return "Bad magician!"


def main(S):
    T=int(S[0])
    for y in range(0,T,1):
        print("")
        x=10*y
        n1=S[x+1][0]
        a1=(S[x+2]).split(" ")
        b1=(S[x+3]).split(" ")
        c1=(S[x+4]).split(" ")
        d1=(S[x+5]).split(" ")
        n2=S[x+6][0]
        a2=(S[x+7]).split(" ")
        b2=(S[x+8]).split(" ")
        c2=(S[x+9]).split(" ")
        d2=(S[x+10]).split(" ")
        s1=grid(n1,a1,b1,c1,d1)
        s2=grid(n2,a2,b2,c2,d2)
        print(("Case #"+str(y+1)+": "+result(ch1(s1,s2))),end="")

        

S=input("Input")
S=S[3:-3]
S=S.split("\n")
l=len(S)
main(S)










        
        
        

                
    
  
