'''
Created on 12-Apr-2014

@author: rajbhagat

working good!!! ha ha ha ha
the force is with me
'''
fileopen=open("C:/Users/rajbhagat/desktop/large.in")
resultopen=open("C:/Users/rajbhagat/desktop/largeres.in",'w')
index=-1
for value in fileopen:
    exiter=seconds=least=total=balance=flag=float(0)
    if index>=0 :
        c,f,x=(value[:-1].split(" "))
        c,f,x=float(c),float(f),float(x)
        print c,f,x
        prod=2.0
        if c<x: 
            while exiter==0:
                seconds+=float(c/prod)
                prod+=f
                total+=c
                val=float (float(x/prod)+seconds)
                if val<least or flag==0:
                    least=val
                if val>least:
                    exiter=1
                flag=1
            if flag==0:
                least= float(x/prod)
        
        elif x<=c:
            least=float(x/2.0)
        print "%0.07f"%least
        prod=2.0
        least1=float(x/prod)
        if least1<least:
            least=least1
        resultopen.write("Case #"+str(index+1)+": "+str("%0.07f"%least)+"\n")
    index+=1
fileopen.close()
resultopen.close()
