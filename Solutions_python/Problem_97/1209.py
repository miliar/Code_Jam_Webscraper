#! /usr/bin/env python
#coding=utf-8

filename = r"C:\Users\i035514\Desktop\Codejam\Qualification\c-small-attempt0"

input=file("%s.in" % filename)
output=file("%s.ou" % filename, "w")
T=int(input.readline())



for caseNum in xrange(1,T+1):
    line = input.readline().rsplit(" ")
    A=int(line[0])
    B=int(line[1])
    Astr=line[0]
    Bstr=line[1]
    result = 0
    length = len(Astr)
    careCircle=False
    careRepeat = False
    circleNum=0
    
    for i in xrange(1,length/2+1):
        if length%i==0:
            careRepeat=True
        else:
            careRepeat=False
        
        if length%2==0 and i%2==1:
            careCircle=True;
        else:
            careCircle=False
        
        xmin = int(Astr[:i])
        xmax = int(Bstr[:i])
        ymin = int(Astr[:length-i])
        ymax = int(Bstr[:length-i])
        xminy = (xmin*(10**(length-i))+ymin,xmin*(10**(length-i))+ymax)
        xmaxy = (xmax*(10**(length-i))+ymin,xmax*(10**(length-i))+ymax)
        yminx = (ymin*(10**i)+xmin,ymin*(10**i)+xmax)
        ymaxx = (ymax*(10**i)+xmin,ymax*(10**i)+xmax)
        total=(xmax-xmin+1)*(ymax-ymin+1)
      
        if A>xminy[0]:
            if A>xminy[1]:
                total=total-(xminy[1]-xminy[0]+1)
            else:
                total=total-(A-xminy[0])
                
        if A>yminx[0]:
            if A>yminx[1]:
                total=total-(yminx[1]-yminx[0]+1)
            else:
                total=total-(A-yminx[0])
        if B<xmaxy[1]:
            if B<xmaxy[0]:
                total=total-(xmaxy[1]-xmaxy[0]+1)
            else:
                total=total-(xmaxy[1]-B)
            
        if B<ymaxx[1]:
            if B<ymaxx[0]:
                total=total-(ymaxx[1]-ymaxx[0]+1)
            else:
                total=total-(ymaxx[1]-B)
        
        if xminy[0]<A and yminx[0]<A:
            total=total+1
        if xminy[1]<A and ymaxx[0]>B:
            total=total+1
        if yminx[1]<A and xmaxy[0]>B:
            total=total+1
        if xmaxy[1]>B and ymaxx[1]>B:
            total=total+1
        
        if careRepeat:
            repeatTimes = length/i
            for x in xrange(xmin,xmax+1):
                value=0
                for t in xrange(0,repeatTimes):
                    value=value+x*(10**(i*t))
                if value<=B and value>=A:
                    total=total-1
        
        if i==2:
            for x in xrange(xmin,xmax+1):
                if not x/10==x%10:
                    value=0
                    for t in xrange(0,length/i):
                        value=value+x*(10**(i*t))
                        valueStr=str(value)
                        firstChar=valueStr[0]
                        lastChar=valueStr[1:]
                        value2=int(lastChar+firstChar)
                    if value<=B and value>=A and value2<=B and value2>=A:
                        circleNum=circleNum+1
            circleNum=circleNum/2
            result=result-circleNum
        
        if i>2 and careCircle:
            total=total-circleNum
        
        if length%2==0 and i == length/2:
            result=result+total/2
        else:
            result = result+total
            
        
    print result
    outstring = "Case #%d: %d\n" % (caseNum, result)
    output.writelines(outstring)

print "Done"
input.close()
output.close()

            
        
        
    
    
    