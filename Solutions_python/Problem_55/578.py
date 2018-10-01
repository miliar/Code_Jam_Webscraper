# -*- coding: utf-8 -*-

import os
import sys


data = open("A-small.in","r")

lines =  data.readlines()

cases = int(lines[0].replace('\n',''))

r = 0
k = 0
n = 0

print cases

lines = lines[1:]

cases_data = []

for i in range(0,cases*2,2):
  print i
  cases_data.append([lines[i].replace('\n',''),lines[i+1].replace('\n','')])


print len(cases_data)

case_n = 0
output = open("output.txt","w")


for data in cases_data:
  case_n = case_n+1
  print case_n
  if case_n!=1:
    temp = '\nCase #'+str(case_n)+': '
  else:
    temp = 'Case #'+str(case_n)+': '
  
  variables = data[0].split()
  R = int(variables[0])
  k = int(variables[1])
  N = int(variables[2])

  groups = data[1].split()
  for i in range(len(groups)):
    groups[i] = int(groups[i])
  
  euros = 0
  t = 0 #number of turns
  for i in range(1,R+1): #each turn
    p = 0 #number of people by turn
    who_in_list = 0
    end_list = []
    for i2 in groups: #each group
      if p+i2<=k: #we can put people
        p = p+i2
        euros = euros + i2
        who_in_list = who_in_list+1
        end_list.append(i2)
      else: #that's it
        #ok, we have our groups to go, now, let's rearrange the list
        groups = groups[who_in_list:]
        for i3 in end_list:
          groups.append(i3)
        break
        
  
  temp = temp+str(euros)
  output.write(temp)

output.close()
print "fin"



  


