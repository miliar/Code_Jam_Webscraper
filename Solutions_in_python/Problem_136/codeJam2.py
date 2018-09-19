'''
Created on 2014-04-11

@author: Tiger
'''

def getTime(c,f,x,i):
    cps =2.0
    time = 0.0
    for i in range(i):
        time += c/cps
        cps+=f
    time+=x/cps
    return time

def getAns(c,f,x,case):
    cps = 2.0
    times =[]
    for i in range(int(x)):
        times.append(getTime(c,f,x,i))
    print "Case #"+str(case)+":", min(times)

f = open ("input2.in","r")
case =1
tests = f.readline().strip()
for i in range(int(tests)):
    d = f.readline().strip().split()
    
    getAns(float(d[0]),float(d[1]),float(d[2]),case)
    
   
    case+=1