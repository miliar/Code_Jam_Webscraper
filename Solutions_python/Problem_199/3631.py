T=int(input())
for counter in range(T):
    temp_input=input().split()
    K=int(temp_input[1])
    S=list(temp_input[0])
    count=flag=0
    running_length=len(S)-(K-1)
    for i in range(running_length):
        if S[i] == "-":
            for ip in range(K):
                if S[i+ip]== "-":
                    S[i+ip]= "+"
                else:
                    S[i+ip]= "-"
                
            count+=1
    remaining=S[i:]
    for remain in remaining:
        if remain=="-":
            flag=1
    if flag==1:     
        print("Case #"+str(counter+1)+": IMPOSSIBLE")
    else:
        print("Case #"+str(counter+1)+": "+str(count))
