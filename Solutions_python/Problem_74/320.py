#!/usr/bin/env python
# encoding: utf-8

import sys

with open(sys.argv[1], 'r') as fin:
    with open('A-small.out', 'w') as fout:
    
        t = int(fin.readline().strip())
        
        for i in xrange(1,t+1):
            
            inplist = fin.readline().split()
            
            n = int(inplist[0])
            
            tup = zip(inplist[1::2], map(int, inplist[2::2]))
            
            #print tup
            
            pos = {'O':1, 'B': 1}
            
            cur = (tup[0][0], 0)
            time = 0

            for (bot, button) in tup:
                #print cur
                if (bot == cur[0]):
                    cur = (bot, cur[1]+abs(pos[bot]-button)+1)
                    pos[bot] = button
                else:
                    time += cur[1]
                    cur = (bot, max(abs(pos[bot]-button)+1 - cur[1], 1))
                    pos[bot] = button
                    
            time += cur[1]                    
                    
            fout.write('Case #{0}: {1}\n'.format(i, time))
                    


                
                
            
    



