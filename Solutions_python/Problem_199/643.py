import math
import time


num = int(input())

i = 1

while i <= num:
    line = input()
    #line = fd.readline()
    #print(line)
    lst = line.split(" ")
    string = lst[0]
    K = int(lst[1])
    l = 0
    mlst = []
    for char in string:
        mlst.append(char)
        l += 1
    ans = 0
    j = 0
    while j < l:
        if mlst[j] == '-':
            if (j+K) > l:
                ans = 'IMPOSSIBLE'
                break
            else:
                for g in range(K):
                    if mlst[j+g] == '-':
                        mlst[j+g] = '+'
                    else:
                        mlst[j+g] = '-'
        
            ans += 1
        j += 1
    
    s = 'Case #' + str(i) + ': ' + str(ans)
    print(s)
    
    i += 1


#print(time.time()-start)

