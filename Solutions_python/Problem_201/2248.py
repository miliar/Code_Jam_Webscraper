import sys
import math

cases = []

with open(sys.argv[1]) as f:
    for i in range(1,int(f.readline())+1):        
        n,k = f.readline().split(' ')
        n,k = int(n),int(k)
        
        e = math.floor(math.log(k,2))
        m = 2**e - 1
        
        space = math.floor((n-m) >> e)
        space -= 1 if k-m > n-m - (space << e) else 0
        
        left = math.floor(space/2)
        right = math.ceil(space/2)
        
        s = 'Case #'+str(i)+': '+ str(right) + ' ' + str(left)  +'\n'
        cases.append(s)

with open(sys.argv[2],'w+') as g:
    g.writelines(cases)          