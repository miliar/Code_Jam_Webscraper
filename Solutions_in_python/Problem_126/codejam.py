import re

num_inputs = int(raw_input())
n={}
name={}
for i in range(num_inputs):
    line = raw_input()
    line=line.split(' ')
    name[i] = re.sub(r'[aeiou]','0',line[0])
    name[i] = re.sub(r'[^0]','1',name[i])
    n[i] = int(line[1])
    
for i in range(num_inputs):
    n_value = 0
    for j in range(n[i], len(name[i])+1):
        for k in range(0, len(name[i])-j+1):
            num_con = 0
            
            for m in range(0, j):
                if name[i][k:j+k][m] == '1':
                    num_con += 1
                else:
                    num_con = 0
                if num_con >= n[i]:
                    n_value += 1
                    break
    print "Case #%s: %s" % (i+1, n_value)
    