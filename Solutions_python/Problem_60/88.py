def calc(n,k,b,time,pos,spd):
    c = 0
    r = 0
    ts = [long(0) for i in range(n)]
    
    for i in range(n-1,-1,-1):
        dis = b - pos[i]
        v = spd[i]
        t = (dis + v - 1)/v
        ts[i] = t
        if t <= time:
            r = r + 1

            for j in range(i,n):
                if ts[j] > time:
                    c = c + 1
            
            if r == k:
                break
        
    #print ts,r,k
    
    if r < k:
        return 'IMPOSSIBLE\n'

    

    return str(c) + '\n'
    

f = open('B-large.in')
fw = open('result.out','w+')

n = int(f.readline())

for i in range(1,n+1):
    fw.write('Case #')
    fw.write(str(i))
    fw.write(': ')
    line = f.readline().replace('\n','')
    datas = line.split(' ')
    n = int(datas[0])
    k = int(datas[1])
    b = int(datas[2])
    t = int(datas[3])

    pos = [long(i) for i in f.readline().replace('\n','').split(' ')]
    spd = [long(i) for i in f.readline().replace('\n','').split(' ')]
    

    l = calc(n,k,b,t,pos,spd)
    
    fw.write(l)

f.close()
fw.close()
