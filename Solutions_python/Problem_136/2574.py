g=open('output2.txt','w')
count=1
with open('B-large.txt','r')  as h :
    m=int(h.readline())
    while m>0 :
        c,f,x=h.readline().split()
        c,f,x=float(c),float(f),float(x)
        if x<=(c*(2+f)/f):
            n=0
        else:
            n=int(((x-c)/c)-(2/f))+1
        i=0
        t=0
        while i<n :
            t= t + c/(2+i*f)
            i=i+1
        t = t + x/(2+n*f)
        t=round(t,7)
        g.write("Case #"+str(count)+": "+str(t)+"\n")
        count=count+1
        m = m-1
g.close()
