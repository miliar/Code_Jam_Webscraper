f=file('input.txt','r')
k=f.read().split('\n')
t=int(k[0])
f_out=file('output.txt','w')
for i in range(t):
    str_input=k[i+1]
    str_input=str_input.split(' ')
    s_max=int(str_input[0])
    prereq=0
    result=0
    for j in range(len(str_input[1])):
        if prereq>=j:
            prereq+=int(str_input[1][j])
        else:
            if j > prereq:
                if str_input[1][j]=='0':
                    continue
                else:
                    result+=j-prereq
                    prereq+=j-prereq
                    prereq+=int(str_input[1][j])
    f_out.write('Case #'+str(i+1)+': '+str(result)+'\n')
f.close()
f_out.close()
