# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 21:46:00 2017

@author: Sachin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:29:20 2017

@author: Sachin
"""
#-+-+-
f = open("B-large.in")
case = 0
first = True
o = open('B-large-out.txt','w')

for line in f:
    if first:
        first = False
        total = int(line)
        continue
    if case-1==total:
        break
   
    case+=1
#Logic comes here
    
    new_num = line.strip()
    line = line.strip()
    
    for i in range(len(line)-1,0,-1):
        if int(new_num[i]) < int(new_num[i-1]):
            new_num = str(int(new_num[:i])-1) + '9'*(len(new_num)-i)
            
    if new_num[0] == '0':
        new_num = new_num[1:]
    
    o.write('Case #'+str(case)+': '+str(new_num)+'\n')

o.close()
f.close()