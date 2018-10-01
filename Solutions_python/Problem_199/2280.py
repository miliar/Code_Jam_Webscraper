t = int(raw_input())
for i in range(t):
    s,k = raw_input().split()
    list1 = list(s)
    k = long(k)
    ans = 0
    flag = 0
    for j in range(len(s)):
        if(list1[j] == '-'):
            ans += 1
            if(j+k-1 >= len(s)):
                flag = 1
                break
            for l in range(k):
                if(j+l+1 <= len(s) and list1[j+l] == '-'):
                    list1[j+l] = '+'
                elif(j+l+1 <= len(s) and list1[j+l] == '+'):
                    list1[j+l] = '-'
#                print ''.join(list1),flag
        
    if(flag == 1):
        print "Case #{}: {}".format(i+1,'IMPOSSIBLE')
    else:
        print "Case #{}: {}".format(i+1, ans)
                
                    







    
