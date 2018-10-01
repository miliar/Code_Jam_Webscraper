
import sys
sys.stdin=open("data.txt")
sys.stdout=open("out.txt","w")
input=sys.stdin.readline

t=int(input())

for cnum in range(t):
    n=input().strip()
    #n=str(cnum+1)
    ans=1
    # pick an index where the number is different
    for i in range(len(n)+1):
        if i==len(n): temp=n
        elif n[i]=='0': continue
        else: temp=n[:i]+str(int(n[i])-1)+'9'*(len(n)-i-1)
        for j in range(len(temp)-1):
            if temp[j]>temp[j+1]: break
        else:
            ans=max(ans,int(temp))
    # check
    if 0:
        temp=n
        for j in range(len(temp)-1):
            if temp[j]>temp[j+1]: break
        else:
            lastval=int(temp)
        if ans<lastval: print("fail",ans,lastval,n)
    print("Case #%d: %d"%(cnum+1,ans))
