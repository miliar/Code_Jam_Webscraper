from math import sqrt
infile = open("C-small-attempt0.in", "r")
lines = infile.readlines()
compiled=[]
for i in lines:
    try:
        if int(i):
            continue
    except ValueError:
        arguments=i.split()
        compiled.append(arguments)
infile.close()
def pal(f):
    a=len(str(f))
    b=0
    for part in str(f):
        if str(f)[a-1]==part:
            b+=1
            a-=1
    if b==len(str(f)):
        return True
    else:
        return False

def square(s):
    c=sqrt(s)
    if c%1==0.0:
        if pal(int((c))):
            return True
        else:
            return False
    else:
        return False
outfile=open("data.txt","w")
cases=0
for l in compiled:
    Tcases=0
    cases+=1
    for a in range(int(l[0]),int(l[1])+1):
        if square(a)==True and pal(a)==True:
            Tcases+=1
        else:
            continue
    outfile.write("Case #")
    outfile.write(str(cases))
    outfile.write(": ")
    outfile.write(str(Tcases))
    outfile.write("\n")
outfile.close()
