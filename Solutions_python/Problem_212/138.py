# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:27:25 2017

@author: tcapon
"""
import itertools
fname = 'A-large.in'
#fname = 'A-small-attempt0.in'
#fname = 'a.in'
oname = fname[:-3]+'.out'
with open(fname,'r') as file:
    with open(oname,'w') as o:
        T = int(file.readline())
        for case in range(1,T+1):
            temp = file.readline().strip().split()
            N = int(temp[0])
            P = int(temp[1])
            print('Case #{}: {},{}'.format(case,N,P))
            groups = [int(x) for x in file.readline().strip().split()]
            print(groups)
            
            order = []
            freshGroups = 0
            # greedy approach: make the smallest sized multiples of P
            while groups:
                for g in groups:
                    #print('G',g)
                    if g % P == 0:
                        #print(g)
                        order.append(g)
                        groups.remove(g)
                        freshGroups = freshGroups + 1
                        break
                else:
                    break
                
            print(groups)
            for r in range(2,len(groups)+1):
                while len(groups) >= r:
                    for p in itertools.combinations(groups,r):
                        #print(p)
                        if sum(p) % P == 0:
                            print(p)
                            freshGroups = freshGroups + 1
                            for x in p:
                                groups.remove(x)
                                order.append(x)
                            break
                    else:
                        break
            
            if groups:
                order.extend(groups)
                freshGroups = freshGroups + 1
            print(order)
            
            o.write('Case #{}: {}\n'.format(case,freshGroups))
            print('Answer: {}'.format(freshGroups))
                