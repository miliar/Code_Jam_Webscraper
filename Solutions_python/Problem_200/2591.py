def solve(n):
    if len(n) == 1:
        return n
    #if n[0]==n[1]:
    #   if n[0] == '1':
    #      return '9'*(len(n)-1)
    #   else:
    #      return str(int(n[0]) - 1) + '9'*(len(n)-1)
    
    i=0
    op = ""
    while i<len(n)-1:
        if int(n[i+1])>int(n[i]):
            op += n[i]
        else:
            ind = i
            b= True
            while i<len(n)-1:
                if n[i+1]<n[i]:
                    b = False
                    break
                i+=1
            if  not b:
                op += str(int(n[ind]) - 1)+'9'*(len(n)-ind-1)
                return str(int(op))
            else:
                return n
        i+=1
    return n

import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()
lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
for i in range(T+1):
    if i==0:
        continue
    line = lines[i]
    ans = solve(line)
    print "Case #"+str(i)+": "+ans