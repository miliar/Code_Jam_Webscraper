t=int(input())
s=''
    
for test in range(t):
    n=input()
    a=list(n)
    for i in range(len(a)):
        if i<len(a)-1 and int(a[i])>int(a[i+1]):
            b=0
            while a[i-b]==a[i-1-b] and i-1-b>-1:
                b+=1
            a[i-b]=str(int(a[i-b])-1)
            a[i+1-b:]='9'*(len(a)-i+b-1)
    
    s+='Case #'+str(test+1)+': '+str(int(''.join(a)))+'\n'
print(s)

