from __future__ import division

import os
import os.path, time
import itertools


fo=open("A-small-attempt0.in")
fw=open("A-small-attempt0.out","w")
n=int(fo.readline())
for p in range(0,n):
        Mat1=[]
        Mat2=[]
        Set1=[]
        Set2=[]
        find=0
        A1=int(fo.readline())
        for i in range(0,4):
                Mat1=Mat1+fo.readline().split()
        A2=int(fo.readline())
        for i in range(0,4):
                Mat2=Mat2+fo.readline().split()
        for k in range((A1-1)*4,(A1-1)*4+4):
                Set1.append(int(Mat1[k]))
        for k in range((A2-1)*4,(A2-1)*4+4):
                Set2.append(int(Mat2[k]))
        for i in range(0,4):
                for j in range(0,4):
                        if Set1[i]==Set2[j]:
                                find=find+1
                                number=Set1[i]
        print find
        
                
        print "Case #"+ str(p+1)+": "
        fw.write("Case #"+ str(p+1)+": ")
        if find==1:
                fw.write(str(number)+"\n")
        elif find == 0:
                fw.write("Volunteer cheated!\n")
        else:
                fw.write("Bad magician!\n")
fw.close()       
        
                





