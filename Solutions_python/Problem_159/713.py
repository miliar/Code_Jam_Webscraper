t = int(raw_input())
for l in range(t):
    s = int(raw_input())
    numbers = map(int, raw_input().split())
    ans=0
    rate=0
    tmp=0
    for i in range(1,s):
        if(numbers[i]<numbers[i-1]):
            tmp=numbers[i-1]-numbers[i]
            if(rate<tmp):
                rate = tmp
            ans+= tmp
    avg=0
    for i in range(s-1):
        if(rate > numbers[i]):
            avg+=numbers[i]
        else:
            avg+=rate

    print "Case #%d: %d %d" %(l+1,ans,avg)
    
