

def checkharmony(lowest, highest, notes):
    for i in xrange(lowest, highest+1):
        isharm=True
        for n in notes:
            if n%i!=0 and i%n!=0:
                isharm=False
        if isharm==True:
            return i
    return "NO"


data=open("C-small-attempt0.in","r").read()


data=data.splitlines()[1:]
data.reverse()
out=open("out.txt","w")
c=0
while data:
    c+=1
    players, lowest, highest=[int(i) for i in data.pop().split(" ")]
    notes=[int(i) for i in data.pop().split(" ")]
    out.write("Case #%i: %s\n"%(c,str(checkharmony(lowest, highest, notes))))
    
    
out.close()
