f1=open("input2",'r')
f2=open("output2.txt",'w')
t=int(f1.readline()[:-1])
for k in range(1,t+1):
    r= str(f1.readline()[:-1])
    s,m=r.split()
    s=list(s)
    m=int(m)
    i = 0
    flag=0
    imp = "IMPOSSIBLE"
    moves = 0
    while i <= len(s) - m:
        if s[i] == '-':
            moves += 1
            for j in range(i, i + m):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
        i = i + 1
    for i in range(0, len(s)):
        if s[i] == '-':
            flag = 1
            break
    if flag == 0:
        f2.write("Case #{}: {}".format(k, moves) + '\n')
    else:
        f2.write("Case #{}: {}".format(k, imp) + '\n')
