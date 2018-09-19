import math

def demo():
    a=open("A-large.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    for i in range(int(b[0])):
        #res=check(b[i*3+2][:-1],b[i*3+3][:-1])
        res=check(b[i+1].split()[1])
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()

def check(r1):
    s,res=0,0
    for i in range(len(r1)):
        res+=int(int(r1[i])>0)*max(0,(i-s-res))
        s+=int(r1[i])
    return res

raw_input("Got data?")
demo()
