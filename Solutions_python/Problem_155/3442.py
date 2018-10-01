p= int(input())
m=p
while(p):
    arr = raw_input().split()
    max_shy = int(arr[0])
    shy = arr[1]
    count = 0
    frnds = 0
    cc=0
    count+=int(shy[0])
    for i in range(1,max_shy+1):
        if shy[i] == '0':
            continue
        cc = i - count
        if cc>0:
            count+=cc
            frnds+=cc
            count+=int(shy[i])
        else:
            count+=int(shy[i])
    print 'Case #%d:'%(m-p+1),frnds
    p-=1
