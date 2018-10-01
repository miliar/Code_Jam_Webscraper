#!/usr/bin/python

lines = [line.strip() for line in open('B-large.in')]
num_case = [int (i) for i in lines[0].split()][0]
for case in range(len(lines)):
   if case == 0:
     continue;
   input= [float (i) for i in lines[case].split()]
   C = input[0]
   F = input[1]
   X = input[2]
   num_farm = int((F * X / C - F - 2) / F + 1)
   num_farm = max(num_farm, 0)
   time = float(0)
   for n in range(num_farm):
       time += C / (2 + F * n)
   print "Case #" + str(case) + ": " + str(time + X / (2 + F * (num_farm)))
   
     
    
