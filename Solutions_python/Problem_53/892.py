'''
Created on May 8, 2010

@author: billy
'''

openfile = open("/home/billy/A-large.in", 'r')
file = open("/home/billy/output2", "w")
info = openfile.readlines()
for k in range(1, len(info)):
    nums = info[k].split(' ')
    strstr = "ON" if int(nums[1]) % 2**int(nums[0]) == 2**int(nums[0]) - 1 else "OFF"
    file.write("Case #" + str(k) + ": " + strstr + "\n")