import time
import math

filename = "A-large.in"

file = open(filename)
out=open(filename.replace("in","out"), 'w')

line_num = 0
cases = 0

line = file.readline()
cases = eval(line)
print 'Number of cases', cases

for case in range(cases):  
    print case + 1
    
    ar1 = file.readline().strip().split(' ')
    max = eval(ar1[0])
    keys = eval(ar1[1])
    al_size = eval(ar1[2])
    
    ar2 = file.readline().strip().split(' ')
    nums = []
    
    for a in ar2:
        nums.append(eval(a))
        
    #print max, keys, al_size
    #print nums
    
    nums.sort()
    nums.reverse()
    
    #print nums
    
    sum = 0
    pos = 0
    for i in nums:
        sum += i * ( 1 + pos / keys)
        pos += 1
    
    #print ''
    
    
    s ="Case #" + str(1+case) + ": " + str(sum)
    print s
    out.write(s + '\n')

    line_num += 1

file.close()
out.close()