import sys, itertools

input_file_name = 'input1.in'
output_file_name = 'output1.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()
num_cases = int(contents.pop(0))
for case in range (num_cases):
    audience = []
    numfriends = 0
    reserve = 0
    line = contents.pop(0)
    a, b = line.split()
    for i in range(len(b)):
        audience.append(int(b[i]))                        
    for i in range(len(audience)):
        if audience[i] == 0:
            if reserve > 0:
                reserve = reserve - 1
            else:
                numfriends = numfriends + 1
        elif audience[i] > 1:
            reserve = reserve + (audience[i] - 1) 
#    print('Case #{}: {}'.format(case+1, numfriends))   
    print('Case #{}: {}'.format(case+1, numfriends), file = f_out)
  
f_in.close()
f_out.close()
