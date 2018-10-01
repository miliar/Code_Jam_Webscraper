T = int(input())

for t in range(T):
    n = input()
    
    ind = 0
    while ind + 1 < len(n):
        if int(n[ind]) > int(n[ind+1]):
            while ind > 0 and n[ind] == n[ind-1]:
                ind -= 1
            break
        else:
            ind += 1
            
    ans = list(n)    
    if ind + 1< len(n):
        ans[ind] = str(int(ans[ind]) - 1)
        for i in range(ind+1, len(n)):
            ans[i] = '9'        
    
    while ans[0] == '0':
        ans.remove('0')
    
    ans = "".join(ans)
    print("Case #{}: {}".format(t+1, ans))