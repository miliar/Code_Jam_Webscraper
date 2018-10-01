import numpy as np

input = open('B-large.in','r')

number_of_cases = input.readline()

# Here's where I'm going to make it into a loop
for i in range(int(number_of_cases)):
     i = i + 1
     current_rate = 2.0
     pussies = input.readline().strip().split()
     cost = float(pussies[0])
     rateincrease = float(pussies[1])
     goal = float(pussies[2])
     new_rate = current_rate + float(rateincrease)
     time1 = float(goal) / current_rate
     time2 = float(cost) / current_rate + float(goal)/ new_rate

     while time1 > time2:
          current_rate = new_rate
          new_rate = current_rate + float(rateincrease)
          time1 = time2
          time2 = time2 - (float(goal)/ current_rate) + (float(cost)/current_rate) + (float(goal)/new_rate)
     print 'Case #%s:' % ( i ), '%1.7f' % ( time1)
          

