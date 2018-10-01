t=int(input())
for t0 in range(t):
    s,k=map(str,input().split())
    k=int(k)
    if len(s)==s.count('+'):
        print("Case #",t0+1,": ",0,sep='')
    else:
        s=list(s)
        ff,c=0,0
        for  i in range(len(s)):
            if s[i] =='-':
                if i+k>len(s):
                    print("Case #",t0+1,": ","IMPOSSIBLE",sep='')
                    ff=1
                    break
                c+=1    
                for j in range(i,i+k):
                    if s[j]=='-':
                        s[j]='+'
                    else:
                        s[j]='-'
            if ff==1:
                break
        if ff!=1:
            print("Case #",t0+1,": ",c,sep='');    