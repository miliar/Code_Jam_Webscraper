# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:03:20 2017

@author: 修修
"""

# -*- coding: utf-8 -*-

with open("B-large.in", "r") as f:
    filein = f.readlines()
        
t = int(filein[0])  # read a line with a single integer
for cnt in range(1, t + 1):
    ans = 0
    N = filein[cnt][:-1]
    #print (N)
    
    if int(N)<10:
        ans = N
    else:
        while True:
            isTidy = 1
            digit = 0
            for digit in range(len(N)-1):
                #print (len(N))
                #print (int(N[cnt]), int(N[cnt+1]))
                
                if int(N[digit]) > int(N[digit+1]):
                    isTidy = 0
                    break
            #print("dig{}".format(digit))#dig>dig+1
            if isTidy == 1:
                ans = int(N)
                break
            else:
                intN = int(N)
                intN -= int(N[digit+1:])
                intN -= 1
                N = str(intN)
                #print("newN"+N)
    
    print ("Case #{}: {}".format(cnt, ans))