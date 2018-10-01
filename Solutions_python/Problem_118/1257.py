import math
foo=open("C-small-attempt0.in","r")
bar=open("fair_op_s.txt","w")
t=int(foo.readline().rstrip())

def IsSquare(x):

    y= 1
    while 1 :
        if x<0 :
            return False
        if x == 0:
            return True
        x -= y
        y += 2
    

i=1
while i<=t:
    ans=''
    count=0
    line=foo.readline().rstrip().split()
    a=int(line[0])
    b=int(line[1])+1
    

    for n in range(a,b) :

        sq=IsSquare(n)

        nS=str(n)
        tS=nS[::-1]
        p1 = nS==tS

        if sq and p1:
            sq1 =str(int(math.sqrt(n)))
            sq2=sq1[::-1]
            p2= sq1==sq2
            if p1 and p2 :
                count+=1
                


    ans="Case #"+str(i)+": "+str(count)
    print ans
    ans=ans+'\n'
    bar.write(ans)        

    i+=1
foo.close()
bar.close()

