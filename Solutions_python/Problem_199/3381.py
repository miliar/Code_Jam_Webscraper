t=int(input())
for case in range(t):
    pan,k=input().split()
    k=int(k)
    pan=list(pan)
    count=0
    for i in range(len(pan)):
        if i>len(pan)-k:
            break
        if pan[i]=='-' :
            count+=1
            #change the symbols
            for j in range(i,i+k):
                if pan[j]=='-':
                    pan[j]='+'
                else:
                    pan[j]='-'

    print('case #',end='')
    print((case+1),end='')

    if '-' in pan :
        print(':',"IMPOSSIBLE")
    else:
        print(':',count)