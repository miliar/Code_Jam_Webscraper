def tidy(s):
    return (s == sorted(s))
'''
def f(n):
    if n<10:
        print(n)
        return
    
    s=list(str(n))
    a=set(s)
    l=len(s)
    if a=={'0','1'}:
        ans='9'*(l-1)
        print(int(ans))
        return
    while tidy(s)==False:
        pos=-1
        for i in range(l-1):
            if s[i+1]<s[i]:
                pos=i+1
                s[i]=str(int(s[i])-1)
                break
        if pos!=-1:
            answer=''.join(s[:pos])+'9'*(l-pos)
            print(answer)
            return
        else:
            print(n)
            return

'''

def f(n):
    if n<10:
        print(n)
        return
    
    s=list(str(n))
    if s==sorted(s):
        print(int(''.join(s)))
        return
    a=set(s)
    l=len(s)
    if a=={'0','1'}:
        ans='9'*(l-1)
        print(int(ans))
        return
    pos=-1
    
    while True:       
        for i in range(l-1):
            if s[i+1]<s[i]:
                pos=i+1
                s[i]=str(int(s[i])-1)
                break
        answer=list(''.join(s[:pos])+'9'*(l-pos))
        x=sorted(answer)
        if answer==x:
            print(int(''.join(answer)))
            break
        


a=[]
n=int(input())
for i in range(n):
    a.append(int(input().strip()))

for i in range(n):
    print("Case #"+str(i+1)+": ",end='')
    f(a[i])

