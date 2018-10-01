inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    args=list(((inp.readline()).rstrip()).split())
    st = args[0]
    K = int(args[1])
    lst = list(st)
    count=0
    for j in range(len(lst)):
        if lst[j]=='-' and len(lst)-j>=K:
            count+=1
            for kk in range(K):
                if lst[kk+j]=='-':
                    lst[kk+j]='+'
                else:
                    lst[kk+j]='-'
    flag=1
    for j in range(len(lst)):
        if lst[j]!='+':
            flag=0
    if flag==1:
        out.write("Case #" + str(i+1) + ": " + str(count) + "\n")
    else:
        out.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")