fil=open('B-large.in','r')
lines=fil.readlines()

numtestcases=int(lines[0].strip())

with open('out5.txt','w') as out:
    for i in range(1,numtestcases+1):
        rate=2.0
        count=0.0
        
        [c,f,x]=lines[i].split()
        c,f,x=float(c),float(f),float(x)
        
        old_worst=x/rate
        count=c/float(rate)
        rate+=f
        new_worst=count+x/float(rate)
        while new_worst<old_worst:
            old_worst=new_worst
            count+=c/float(rate)
            rate+=f               
            new_worst=count+x/float(rate)
            
        
        out.write("Case #%d: %0.7f\n" %(i,old_worst))

    