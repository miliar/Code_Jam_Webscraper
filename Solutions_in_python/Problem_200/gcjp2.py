# def correct(n):
#     s = str(n)
#     for i in range(1,len(s)):
#         if int(s[i]) < int(s[i-1]):
#             return False
#     return True
    
for xyz in range(int(input())):
    s = input()
    n = int(s)
    l = len(s)
    s = list(s)
    print("Case #"+str(xyz+1)+':',end=' ')
    if n < int('1'*l):
        print('9'*(l-1))
        ans1 = int('9'*(l-1))
    else:
        for i in range(l-2,-1,-1):
            if int(s[i+1]) < int(s[i]):
                s[i] = str(int(s[i])-1)
                for j in range(i+1,l):
                    s[j] = '9'
        ans1 = int("".join(s))        
        print("".join(s))
        
    # for i in range(n,-1,-1):
    #     if correct(i):
    #         print(i)
    #         ans2 = i
    #         break

    # if ans1 != ans2:
    #     print("------------")
    #     print(s)
    #     print(n)
    #     print(l)
    #     print(ans1)
    #     print(ans2)
    #     print("------------")        
