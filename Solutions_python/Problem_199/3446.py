# your code goes here
from sys import stdin

t = int(stdin.readline().strip())
for iii in range(t):
        tmp = stdin.readline().strip().split()
        k = int(tmp[1])
        s = []
        for  i in range(len(tmp[0])):
                a=0 if tmp[0][i]=='-' else 1
                s.append(a)
        ans = 0
        for i in range(len(s)-k+1):
                if s[i]==0:
                        for j in range(k):
                                s[i+j]=1 if s[i+j]==0 else 0
                        ans+=1
        for i in range(len(s)):
                if s[i]==0: ans=-1
        if ans>=0: print('Case #{0}: {1}'.format(iii+1,ans))
        else: print('Case #{0}: IMPOSSIBLE'.format(iii+1))
