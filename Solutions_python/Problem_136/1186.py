'''
Created on 12-Apr-2014

@author: savs95
'''
#to find the rounding function .  . . . .in python 
gamma=open("input.in","r")
hilde=open("output.txt","w")
n=int(gamma.readline())
i=0
while(i<n):
    line=gamma.readline().split()
    C=float(line[0])
    F=float(line[1])
    X=float(line[2])
    cookie_rate=2.0
    time_taken=0.0;
    cookies=0.0;
    while(((C/cookie_rate)+(X/(cookie_rate+F)))<(X/cookie_rate)):
        time_taken+=(C/cookie_rate)
        cookie_rate+=F
    time_taken+=(X/cookie_rate) # Dont know function to round off to a relative value :(
    asnwer1="Case #"+str(i+1)+": "+str(round(time_taken,7))+"\n"
    hilde.write(asnwer1)
    i+=1
hilde.close()
gamma.close()