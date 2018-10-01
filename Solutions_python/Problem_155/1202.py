import numpy as np
f = open('./A-small-attempt0.in')
f.close()
case = lines[0]
case=case.strip('\n')
need = []
for i in range(0,int(case)):
    line = lines[i+1]
    line=line.strip('\n')
    strs = line.split(' ')
    s_max = int(strs[0])
    need_num = 0
    if (s_max == 0):
        need.extend(str(need_num))
        continue
    n = [ int( strs[1] ) for strs[1] in strs[1] if strs[1] ]
    
    have_num = n[0]
    for i in range(1, s_max+1):
        if ((i > have_num + need_num) and (n[i] > 0) ):
            need_num += i - (have_num + need_num);
        have_num += n[i];
    need.extend(str(need_num))
f = open('./output.txt','wb')
for i in range(0, int(case)):
    s = "Case #" + str(i+1) +": "+(need[i])+"\n"
    f.write(s)
f.close()
