import sys

fin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')

t = int(fin.readline())

#for every case
for x in range(t):
    data = fin.readline().strip('\n').split(' ')
    
    c = int(data[0])
    cs = data[1:1+c]
    data = data[1+c:]

    d = int(data[0])
    ds = data[1:1+d]
    data = data[1+d:]

    n = data[0]
    invoke = data[1]

    # Now i have all my data
    cl = []
    for y in range(8):
        cl.append([None]*8)
    el = {'Q':0, 'W':1, 'E':2, 'R':3, 'A':4, 'S':5, 'D':6, 'F':7}
    for comb in cs:
        a1,a2,a3 = comb
        a1,a2 = el[a1],el[a2]
        cl[a1][a2],cl[a2][a1] = a3,a3


    # Invoke time
    ilist = []
    exist = [0]*8
    for e in invoke:
        ilist.append(e)
        exist[el[e]] += 1
        
        # Do combination
        if len(ilist) >= 2 and ilist[-2] in 'QWERASDF':
            a1,a2 = ilist[-1],ilist[-2]
            a1,a2 = el[a1],el[a2]
            if cl[a1][a2]:
                ilist[-2:] = [cl[a1][a2]]
                exist[a1] -= 1
                exist[a2] -= 1
            
        # Do oppositions
        for op in ds:
            if exist[el[op[0]]] and exist[el[op[1]]]:
                exist = [0]*8
                ilist = []
                
    
    print('Case #'+str(x+1)+': [', end='')
    for element in ilist[:-1]:
        print(element, end=', ')
    if len(ilist) > 0:
        print(ilist[-1], end=']\n')
    else:
        print(']')

sys.stdout.close()
fin.close()
