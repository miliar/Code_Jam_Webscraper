#!/usr/bin/python
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np

# <codecell>

with open('D-large.in') as fIn:
    n_case = int(fIn.readline())
    for i in range(n_case):
        n_blocks = int(fIn.readline())
        line = fIn.readline()
        naomi_list = np.array([float(k) for k in line.split()])
        line = fIn.readline()
        ken_list = np.array([float(k) for k in line.split()])
        naomi_list.sort()
        ken_list.sort()
        #vi = np.argsort(naomi_list, axis=0)[::-1]
        #naomi_list_i = naomi_list[vi]
        
        naomi_list_war1 = naomi_list
        ken_list_war1 = ken_list   
      #  print naomi_list
      #  print ken_list
        for n in range(len(naomi_list_war1)):
            index = np.where(ken_list_war1>naomi_list_war1[n])
            if len(index[0]) == 0:
                n=n-1
                break
            #print index
            ken_list_war1 = np.delete(ken_list_war1,np.s_[0:index[0][0]],0)
           # print 'ken_list:',ken_list_war1, n
            if len(ken_list_war1)==0:
                break
            ken_list_war1 = np.delete(ken_list_war1,0,0)
            if len(ken_list_war1)==0:
                break            
        war_score_1 = len(naomi_list_war1)-n-1
        
        naomi_list_war2 = naomi_list
        ken_list_war2 = ken_list
        war_2 = np.greater(ken_list_war2,naomi_list_war2)
        while True in war_2:
            naomi_list_war2 = np.delete(naomi_list_war2,0,0)
            ken_list_war2 = np.delete(ken_list_war2,-1,0)
            if len(naomi_list_war2)==0:
                break
            war_2 = np.greater(ken_list_war2,naomi_list_war2)
        war_score_2 = len(naomi_list_war2)
       # war_score_2 = np.greater(ken_list,naomi_list_i)
        print 'Case #{0}:'.format(i+1), war_score_2, war_score_1
      #  print naomi_list_i
      #  print np.greater(ken_list,naomi_list)
      #  print war_score_2

# <codecell>


