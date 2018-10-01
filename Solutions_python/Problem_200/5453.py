# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


data_in = open("B-small-attempt1.in", 'r')
data_out = open("result.txt", 'a')

test_count = int((data_in.readline()).strip())


for test in range(test_count):
   digit_stack = []
   test_number = (data_in.readline()).strip()
   done = False
   for digit_id in range(len(test_number)):
       if done:
           break
       new_digit= test_number[digit_id]
       if digit_stack == []:
           digit_stack.append((int(new_digit),digit_id))          
       else:
           x,y = digit_stack.pop()          
           if int(new_digit)>x:
               digit_stack.append((x,y))
               digit_stack.append((int(new_digit),digit_id))
           elif int(new_digit)<x:
               decrement_value = x-1
               if decrement_value == 0:
                   digit_stack.append((9,1))
                   done = True
                   break
               elif len(digit_stack)==0 or decrement_value > ((digit_stack[-1])[0]):
                   digit_stack.append((decrement_value, y))
                   digit_stack.append((9,y+1))
                   done = True
                   break
               digit_stack.append((9,digit_id))
               done = True
           else:
               digit_stack.append((x,y))
   working_digit = len(test_number)
   result = ""
   while len(digit_stack)>0:
       r,t = digit_stack.pop()
       result = ((str(r)+"")*(working_digit-t))+ result
       working_digit = t
   data_out.write("Case #{0}: {1}\n".format(test+1, result))
   

data_out.close()
data_in.close()
               
                   
                   
                   
            
