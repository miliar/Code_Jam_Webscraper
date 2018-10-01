__author__ = 'franyell'



def getM(f1,line):
    m1=[]
    for j in [1,2,3,4]:
        l= f1.readline()
        if j==line:
            m1= [ int(x) for x in l.split(' ') ]
    return m1

def getAnswer(m1,m2):
    val=0
    times=0
    for x in m1:
        if x in m2:
            val=x
            times+=1
        if times>1:
            return [2, 0]
    if times==0:
        return [0,val]
    return [1, val]


f1= open("input.txt")
f2=open("output.txt","w")
cases=int(f1.readline())
for i  in range(1,cases+1):
    ans1= int(f1.readline())
    m1=getM(f1,ans1)
    ans2= int(f1.readline())
    m2=getM(f1,ans2)
    r=getAnswer(m1,m2)

    if r[0]==2:
        f2.write("Case #"+str(i)+ ": Bad magician!\n")
    elif r[0]==1:
        f2.write("Case #"+str(i)+ ": "+str(r[1])+"\n")
    else:
         f2.write("Case #"+str(i)+ ": Volunteer cheated!\n")
