from __future__ import division

import os
import os.path, time
import itertools

def tidy(Line):
        dirty=False
        att=1
        while dirty or att==1:
                dirty=False
                arr=[int(x) for x in Line]
                start_dirt=len(arr)
                for i in range(1,len(arr)):
                        if arr[i]<arr[i-1]:
                                dirty=True
                                start_dirt=i-1
                                break
                        
                linenew=""
                if dirty:
                        for i in range(0,len(arr)):
                                if i==start_dirt:
                                        arr[i]=arr[i]-1
                                if i>start_dirt:
                                        arr[i]=9
                                linenew=linenew+str(arr[i])
                else:
                        linenew=Line
                att=att+1
                Line=linenew

        
                
        return linenew
        

        


#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("B-small-attempt0.in")
#fw=open("B-small-attempt0.out","w")
fo=open("B-large.in")
fw=open("B-large.out","w")

n=int(fo.readline())
for k in range(0,n):
        Line=fo.readline().rstrip()
        
        print "Case #"+ str(k+1)+": "
        print Line
        print int(tidy(Line))
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(str(int(tidy(Line)))+"\n")         
fw.close()        
        
                





