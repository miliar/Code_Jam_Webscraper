def flip(i,k,lis):
    for j in range(i,k+i):
        if lis[j] == '+':
            lis[j] = '-'
        else:
            lis[j] = "+"
    return lis


t = int(raw_input())
for i in range(0,t):
    pan,k = raw_input().split()
    pan = list(pan)
    k = int(k)
    ans = 0
    for j in range(0,len(pan)):
        if j == len(pan) - 1 and pan[j] == '+':
            print "Case #"+str(i+1)+": "+str(ans)
        elif pan[j] == '-':
            if len(pan) - j < k:
                print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
                break
            pan = flip(j,k,pan)
            ans = ans + 1
        
