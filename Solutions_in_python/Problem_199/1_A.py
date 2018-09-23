

def check(s):
    for i in range(len(s)):
        if(s[i]=='-'):
            return False
    return True
def count(s, k, start, number):
    global ans
    if(k+start==len(s)):
        if(check(s)):
            ans=min(ans, number)
        for i in range(k):
            if(s[start+i]=='+'):
                s=s[:start+i]+'-'+s[start+i+1:]
            else:
                s=s[:start+i]+'+'+s[start+i+1:]          
        number+=1
        if(check(s)):
            ans=min(ans, number)
        for i in range(k):
            if(s[start+i]=='+'):
                s=s[:start+i]+'-'+s[start+i+1:]
            else:
                s=s[:start+i]+'+'+s[start+i+1:]        
        number-=1
    else:
        count(s, k, start+1, number)
        for i in range(k):
            if(s[start+i]=='+'):
                s=s[:start+i]+'-'+s[start+i+1:]
            else:
                s=s[:start+i]+'+'+s[start+i+1:]          
        number+=1
        count(s, k, start+1, number)
        for i in range(k):
            if(s[start+i]=='+'):
                s=s[:start+i]+'-'+s[start+i+1:]
            else:
                s=s[:start+i]+'+'+s[start+i+1:]         
        number-=1        
        
f=open("A.in", 'r')
g=open("A_sol.txt", 'w')
T=int(f.readline().strip())
for i in range(T):
    temp=f.readline().strip().split()
    ans=999
    count(temp[0], int(temp[1]), 0, 0)
    if(ans==999):
        g.write("Case #%d: Impossible\n"%(i+1))
    else:
        g.write("Case #%d: %d\n"%(i+1, ans))
f.close()
g.close()