from math import ceil
In = open("D:\\Workspace\\Google Code Jam\\B-small-attempt3.in", 'r')
Out = open("D:\\Workspace\\Google Code Jam\\Out.py", 'w')
T = int(In.readline())
for ttt in range(T):
    D = int(In.readline())
    li = []
    for i in In.readline().split():
        li.append(int(i))
    li = sorted(li)
    li.reverse()
    time = [li[0]]
    m = li[0]
    
    for i in range(1,m+1):
        lix = []
        for item in li:
            lix.append(item)
        for j in range(m):
            li0 = lix[0]
            lix[0] = li0 - i
            lix.append(i)
            lix = sorted(lix)
            lix.reverse()
            time.append(lix[0] + j + 1)
        
    Out.write('Case #{}: {}\n'.format(ttt+1, min(time)))
    
In.close()
Out.close()