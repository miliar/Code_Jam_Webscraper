import sys

j=1
first_row=[]
second_row=[]
intersect=[]
of=open("output.out","w+")
fo= open("B-large.in","r+")

no_of_cases=int(fo.next())

for line in fo:
    total_time=0.0
    values=line.split()

    c=float(values[0])
    f=float(values[1])
    x=float(values[2])
    rate=2.0
    if(x<=c):
        total_time=x/rate
    else:
        while(1):
            
            if((x/rate)<((c/rate)+(x/(rate+f)))):
                total_time+=x/rate
                break
            else:
                total_time+=c/rate
                rate=rate+f    
    of.write("Case #"+str(j)+": "+"%.7f" %total_time+"\n")            
    j+=1

of.close()
fo.close()        