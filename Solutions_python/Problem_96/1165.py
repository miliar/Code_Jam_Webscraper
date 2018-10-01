#!/usr/bin/env python
import sys

def dancer(filename1,output_name1):
    file1=open(filename1,'r')
    lines=file1.readlines()
    
    file2=open(output_name1,'w')
    length=len(lines)
    total=int(lines[0].strip("\r\n"))
    index=1
    for i in range(total):
        record=lines[index].strip("\r\n").split(" ")
        newrecord=[int(k) for k in record]
        number_dancer=newrecord[0]
        number_surprise=newrecord[1]
        p=newrecord[2]
        value=0 #maximum_possible
        value2=0 #total number of numbers greater than or equal to p
        for item in newrecord[3:]:
            if item>=p:
                if item+2>=p*3:
                    value+=1
                if item+4>=p*3:
                    value2+=1
        value2=value2-value
        if value2<=0:
            pass
        else:
            if value2>=number_surprise:
                value=value+number_surprise
            else:
                value=value+value2
        if value>number_dancer:
            value=number_dancer
        file2.write("Case #%s: %s\n" %(i+1,value))    
        index=index+1
    
if __name__=="__main__":
    dancer(sys.argv[1],sys.argv[2])
