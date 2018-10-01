from sys import stdin

cases = int(input())
for i in range(cases):
    string = input().split()
    #print(string)
    string[1] = int(string[1])
    if len(string[0])<string[1]:
        print("Case #{}: {}".format(i+1, "IMPOSSIBLE"))
        continue
    cnt = 0
    s = list(string[0])
    for j in range(len(string[0])-string[1]+1):
        if s[j] == '-':
            cnt+=1
            for k in range(string[1]):
                if s[j+k] == '-':
                    s[j+k] ='+'
                else:
                    s[j+k] = '-'
                #print(s[0])
    #print(s[0])
    #print(s)
    check = 0

    for j in range(len(s)):
        if s[j]=='-':
            check = 1
            break
    #print(check)
    if(check):
        print("Case #{}: {}".format(i+1, "IMPOSSIBLE"))

    else:
        print("Case #{}: {}".format(i+1, cnt))
