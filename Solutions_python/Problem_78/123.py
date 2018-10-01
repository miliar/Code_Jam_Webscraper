#!/usr/bin/env python
# -*- coding: utf-8 -*-



if __name__ == "__main__":

    
    
    inFile = open("A-large.in","r")
    outFile = open("practice.out","w")
    
    caseNum = int(inFile.readline())

    for i in xrange(1,caseNum+1):
       
	N,PD,PG = map(int,inFile.readline().split())
	print N,PD,PG
        flag = False
        if (PD<PG and PG ==100) or (PD>PG and PG ==0):
            outFile.write("Case #%d: Broken\n" % (i,))
        else:
            if N>100:
                N = 100
            if PD == 0:
                outFile.write("Case #%d: Possible\n" % (i,))
            else:
                for j in range(1,N+1):
                    if (j*100 % PD == 0) and (j*100/PD <= N):
                        outFile.write("Case #%d: Possible\n" % (i,))
                        flag = True
                        break
                if not flag:
                    outFile.write("Case #%d: Broken\n" % (i,))      
           
                
        
        
        
       
        
    outFile.close()
    inFile.close()
