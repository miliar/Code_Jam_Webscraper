def sol(N):
 Ns=str(N)
 if int(''.join(sorted(Ns)))==N: return N
 else:
  i=0
  while Ns[i+1]>=Ns[i]: i+=1
  return sol(int(Ns[:i]+str(int(Ns[i])-1)+'9'*(len(Ns)-i-1)))

inp=file('B-large.in','rb+'); out=file('B-large.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 N=int(inp.readline().strip())
 out.write('Case #%i: %i\r\n'%(t,sol(N)))