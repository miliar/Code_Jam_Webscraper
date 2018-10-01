import sys
sys.setrecursionlimit(100000)


def getTidy(n):
    #print n
    temp = n[0]
    for i in range(len(n)):
        if n[i] < temp:
            n[i-1] -= 1
            j = i
            n[i:] = [9]*(len(n)-i)
            #print "inside" + str( n)
            return getTidy(n)
        temp = n[i]
    return n
            
            

            
p1 = open('file','r')
p = p1.read().split('\n')[1:-1]
i = 1
o = open('out.txt','w')
for l in p:
    k = map(lambda x:int(x),list(l))
    t = getTidy(k)
    j = 0
    while j < len(t) and t[j] == 0 :
        j += 1
    if j == len(t):
        res = [0]
    else:
        res = t[j:]
    t = ''.join(map(lambda x: str(x),res))
    o.write('Case #' + str(i) + ': ' + t + '\n')
    i += 1
    
    
p1.close()
o.flush()
o.close()