def last_tidy(x):
    y=list(str(x))
    if sorted(y)==list(str(x)):
        return x
    x=x-1
    ch=True
    while ch:
        y1=list(str(x))
        if sorted(y1)==list(str(x)):
            return x
        x=x-1
f=open("B-small-attempt0.in.txt",'r')
x=list(f.readlines())

for i in range(len(x)):
    x[i]=int(x[i])
print x[66]

for i in range(1,len(x)):
    print "Case #"+str(i)+":"+str(last_tidy(x[i]))