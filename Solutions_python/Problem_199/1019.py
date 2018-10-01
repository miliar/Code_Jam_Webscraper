  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import os
os.chdir("D:/JC/Codejame2017")
#import fileinput
#import sys

f = open('A-large.in')
t = int(f.readline())

def flip (str1):
    ans = ''
    for j in str1:
        if j == '+':
            j = '-'
            ans += j
        else:
            j ='+'    
            ans += j
    return ans

def all_same(items):
    return all(x == items[0] for x in items)

target = open('q1-L.txt', 'w')

for i in range(t):
   s1,k = f.readline().strip().split(" ")
   s1 = list(s1)
   k = int(k)
   flips = 0
   length = len(s1)
   res = ''
   for j in range(length):
       #print(s1)
       if(j+k <= length):
           if (s1[j] == '-'):
               s1[j:j+k] = flip(s1[j:j+k])
               flips +=1
       else:
           if (all_same(s1)):
               res =  str(flips) 
           else:
               res = 'IMPOSSIBLE'    
   line = "Case #{}: {}".format(i+1, res) 
   if(i <= t-2):          
       target.write(line)
       target.write("\n")
target.write(line)  
target.close()
   #print("Case #{}: {}".format(i+1, res))    
               
           
#t = int(fileinput.input('pancakes1.txt'))  # read a line with a single integer)
#for i in range(1, t + 1):
#  s1,k = input().strip().split(" ")  # read a list of integers, 2 in this case
# # print("Case #{}: {} {}".format(i, n + m, n * m))
