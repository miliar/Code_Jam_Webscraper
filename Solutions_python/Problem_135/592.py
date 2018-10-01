#!/usr/bin/python
__author__ = 'Jin'

import sys
#sys.argv[0] input
#sys.argv[1] output file


#get the input data
#open the file
read = open(sys.argv[1],"r");
write = open(sys.argv[2],"w");
data = read.readlines()
read.close()

test_cases = data.pop(0)

result = range(int(test_cases))
for i in range(0,int(test_cases)):
    answer =data.pop(0).strip()
    row1 = data.pop(0).strip()
    row2 = data.pop(0).strip()
    row3 = data.pop(0).strip()
    row4 = data.pop(0).strip()

    if(answer=="1"):
        keep = row1
    elif(answer == "2"):
        keep = row2
    elif(answer == "3"):
        keep = row3
    elif(answer == "4"):
        keep = row4
    


    answer = data.pop(0).strip()
    row1 = data.pop(0).strip()
    row2 = data.pop(0).strip()
    row3 = data.pop(0).strip()
    row4 = data.pop(0).strip()
    compare1 =[]
    compare2 = []
    if(answer == "1"):
      compare1 = keep.split()
      compare2 = row1.split()
      
    elif(answer == "2"):
        
      compare1 = keep.split()
      compare2 = row2.split()
    elif(answer == "3"):
      compare1 = keep.split()
      compare2 = row3.split()
    elif(answer == "4"):
      compare1 = keep.split()
      compare2 = row4.split()
 
    count = 0
    num = 0
    for x in compare1:
        if x in compare2:
          count+=1
          num = x
    if(count >=2):
        result[i] = "Bad magician!"
    elif(count == 1):
        result[i] = num
    elif(count == 0):
        result[i] = "Volunteer cheated!"
    
    write.write('Case #'+str(i+1)+': '+result[i]+"\n")
write.close()
