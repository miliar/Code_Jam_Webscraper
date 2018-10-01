T = int(input())

for j in range(T):
    l = input().split(" ")
    s = list(l[1])
    number = int(s[0])
    friends = 0
    
    for i in range(1,int(l[0])+1):
        
        if number >= i :
            number += int(s[i])
            
        else:
            friends += i - number 
            number += int(s[i]) + (i - number)    
            
    print("Case #" + str(j+1) + ": " + str(friends))    
