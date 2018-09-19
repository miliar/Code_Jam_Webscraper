'''
Created on 13.04.2014

@author: Verethragna
'''

path = input('Eingabedatei: ')
rid = open(path)
oid = open(path+".out", "w")

N = int(rid.readline())

for i in range(1,N+1,1):
    T = int(rid.readline())
    wN = sorted(list(map(float, rid.readline().rstrip('\n').split(' '))))
    wKW = sorted(list(map(float, rid.readline().rstrip('\n').split(' '))))
    wKD = list(wKW)
    
    y = z = 0
    l = T - 1
    for j in range(l, -1, -1):
        k = j
        while k >= 0 and wKW[k] > wN[j]:
            k -= 1
        if k == j:
            z += 1
            k = 0
        else:
            k += 1
        wKW.pop(k)
        
        if l >= 0:
            while l >= 0 and wN[j] < wKD[l]:
                l -= 1
            if l >= 0:
                l -= 1
                y += 1
    
    oid.write('Case #' + str(i) + ': ' + str(y) + ' ' + str(z) + '\n')

rid.close()
oid.close()