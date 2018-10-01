T= int(input())

for case in range(T):
    line= input().split()
    S= list(line[0]); K= int(line[1])

    count=0
    for i in range(len(S)-K+1):
        if S[i]=='-':
            for j in range(i,i+K):
                S[j]= '+' if S[j]=='-' else '-'
            count+=1

    impossible=False
    for a in S:
        if a=='-':
            impossible=True

    print("Case #"+str(case+1)+": "+("IMPOSSIBLE" if impossible else str(count)))
