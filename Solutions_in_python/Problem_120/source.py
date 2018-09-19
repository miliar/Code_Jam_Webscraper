import math
theInput = open('A-small-attempt5.in','r')
theOutput = open ('outputnew2.out','w')

numTest = int(theInput.readline())
for x in xrange(0,numTest):
    cnt = 0
    thisLine = theInput.readline() 
    r = int(thisLine[0:thisLine.find(' ')])
    t = int(thisLine[thisLine.find(' ')+1:])
    r = r+1;
    t = t-(math.pi*(2*r-1))/math.pi;
    cnt= cnt+1
    while (t > 0):
        r = r + 2;
        t = t-(math.pi*(2*r-1))/math.pi;
        if t+0.5 < 0 :
            break;
        cnt=cnt+1
    theOutput.write("Case #"+str(x+1)+": "+ str(cnt)+ "\n")
theInput.close()
theOutput.close()
