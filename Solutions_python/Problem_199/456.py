import sys
sys.setrecursionlimit(1010)

def sol(S,K,topmost=True):
 if len(S)>K:
  if S[0]=='+': out=sol(S[1:],K,False)
  else: out=1+sol(''.join([{'-':'+','+':'-'}[s] for s in S[1:K]])+S[K:],K,False)
 elif len(S)==K: out = 1 if S=='-'*K else 0 if S=='+'*K else -1000000
 if not topmost: return out
 else: return (out if out>=0 else 'IMPOSSIBLE')

inp=file('A-large.in','rb+'); out=file('A-large.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 S,K=inp.readline().strip().split(' '); K=int(K)
 out.write('Case #%i: %s\r\n'%(t,sol(S,K)))