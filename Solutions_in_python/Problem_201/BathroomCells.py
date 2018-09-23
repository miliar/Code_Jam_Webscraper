# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 20:56:29 2017

@author: Sachin
"""



from Queue import PriorityQueue

case = 0
o = open('C-small-1-attempt0-out.txt','w')
with open('C-small-1-attempt0.in' , 'r') as f:
    first_line = f.readline()
    for line in f:
        case+=1
        s_list = PriorityQueue()
        cells, people = [int(x) for x in line.split(' ' )]
        s_list.put((-cells, cells))
        ls = 0
        rs = 0
        for i in range(people):
            large = s_list.get()[1]
            if large == 1:
                ls = 0
                rs = 0
                
            elif large%2 == 0:
                rs = large/2
                ls = rs-1
                
            else:
                rs = large/2
                ls = rs
            s_list.put((-ls,ls))
            s_list.put((-rs,rs))
    
        o.write('Case #'+str(case)+': '+str(rs)+ ' '+ str(ls)+'\n')
    
o.close()
        
