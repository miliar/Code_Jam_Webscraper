fp=open("B-large.in",'r')
fo=open("B-large.out",'w')
line=fp.readline()
l=line.replace("\n","")
for testNumber in range(int(l)):
    line=fp.readline()
    line=line.replace("\n","")
    splitted=line.split(" ")
    c=float(splitted[0])
    f=float(splitted[1])
    x=float(splitted[2])
    thresholdTime=x/2
    if (c/2)>(x/2):
        answer=x/2
        #print answer
        fo.write("Case #"+str(testNumber+1)+": "+str(answer)+"\n")
    else:
        originalNumberOfCookiesPerSecond=2
        revisedNoOfCookiesPerSec=2
        count=1
        tp1=0.0
        tx1=0.0
        ptp1=0.0
        ptx1=0.0
        n=[]
        answer=0
        totalTime=0.0
        ptotalTime=thresholdTime
        while thresholdTime>totalTime:
            tp1=c/revisedNoOfCookiesPerSec
            tx1=x/(f*count+2)
            totalTime=tp1+tx1+ptp1
            if totalTime>ptotalTime:
                answer=ptotalTime
                break
            ptotalTime=totalTime
           
            n.append(totalTime)
            ptp1=ptp1+tp1
            tp1=0
            revisedNoOfCookiesPerSec=2+(f*count)
            count=count+1
        fo.write("Case #"+str(testNumber+1)+": "+str(round(ptotalTime,8))+"\n")
fp.close()
fo.close()

            
            
        
    
