#2012 codejam problem 1


def getit(alist):
    res =0
    tabl ={}
    A = int(alist[0])
    B = int(alist[1])
    cap = pow(10, len(alist[1:]))
    n =A
    while n <B:
        temp=[]
        nn = str(n)
        n1 = len(nn)
        n2 =0
        tu = False
        for k in nn[1:]:
            if k !=nn[0]:
                tu =True            
        while n2 < n1 and n1>1 and tu:
            tmp =int(nn[n2:]+nn[:n2])
            if tmp>n and tmp <=B and tmp not in temp:
                #print nn, tmp
                temp.append(tmp)
            n2 +=1
        res += len(temp)
        if len(temp) !=0:
            tabl[n]=temp
        n +=1
    return tabl
    
def comp(alist):
    res =0
    global pretable
    A = int(alist[0])
    B = int(alist[1])
    n =A
    while n <B:
        if n in pretable:
            temp = pretable[n]
            for k in temp:
                if k <=B:
                    res +=1
        n +=1

    return res

in1 = open(r'c:\users\douglas\documents\home\yiqiang\2012codejam\c-large.in')
out1 = open(r'c:\users\douglas\documents\home\yiqiang\2012codejam\clargeout.txt', 'w')
lines = in1.readline()
n = int(lines.rstrip())
pretable = getit(['1', '2000000'])
print 'Ok'
m=1
result=[]
lines =in1.readline()
while lines !='':
    temp = lines.rstrip().split()
    res = comp(temp)
    print 'donecomp'
    result.append(res)    
    lines =in1.readline()

for key in result:
    out1.write("Case #"+str(m)+': '+str(key)+'\n')
    m+=1
in1.close()
out1.close()
