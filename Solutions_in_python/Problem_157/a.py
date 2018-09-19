dic = {'ii':(-1,''),'jj':(-1,''),'kk':(-1,''),'ij':(1,'k'),'ik':(-1,'j'),'ji':(-1,'k'),'jk':(1,'i'),'ki':(1,'j'),'kj':(-1,'i')}
cache = {}
def solver(data):
    return ret(data,'ijk',1)
def ret(data,aim,flag):
    if (data,aim,flag) in cache:
        return cache[data,aim,flag]
    tempcache=set()
    while len(data)>len(aim) and len(data)>1:
        tempcache.add((data,aim,flag))
        if aim and data[0] == aim[0]:
            tres =  ret(data[1:],aim[1:],flag)
            cache[(data[1:],aim[1:],flag)] =tres
            if tres:
                return True
        a,b = dic[data[:2]]
        flag *= a
        data = b+data[2:]
    cache.update({key: ((data == aim or (not data and not aim)) and flag == 1) for key in tempcache})
    return True if  ((data == aim or (not data and not aim)) and flag == 1) else False

res = []
with open('1.in','r') as infile:
    n = int(infile.readline())
    for i in range(n):
        k = int(infile.readline().strip().split(' ')[-1])
        tmp = infile.readline().strip()
        data = ""
        for j in range(k):
            data +=tmp
        res.append("Case #%d: %s" %(i+1,"YES" if solver(data) else "NO"))
with open('1.txt','w') as out:
    out.write('\n'.join(res))
