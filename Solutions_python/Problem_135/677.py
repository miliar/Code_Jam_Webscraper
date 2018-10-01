def fn():
    a = []
    a1 = int(raw_input())-1
    for i in range(4):
        tmp = map(int,raw_input().split())
        if (i==a1):
            a = tmp
    b = []
    a2 = int(raw_input())-1
    for i in range(4):
        tmp = map(int,raw_input().split())
        if (i==a2):
            b = tmp

    
    aa = []
    for i in a:
        if i in b:
            aa.append(i)
            
    if len(aa)== 0:
        return "Volunteer cheated!"
    if len(aa)== 1:
        return aa[0]
    else:
        return "Bad magician!"
            
        


t = int(raw_input())

for i in range(t):
    print "Case #"+str(i+1)+": "+str(fn())

