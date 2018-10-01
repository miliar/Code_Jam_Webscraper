import math

def sol(N,P,serving,ingpacks):
 #print N,P,serving,ingpacks
 for i in range(N):
  ingpacks[i]=[(int(math.ceil((j*10.)/(serving[i]*11))),(j*10)/(serving[i]*9)) for j in ingpacks[i]]
  ingpacks[i]=sorted(filter(lambda p: p[0]<=p[1], ingpacks[i]))
 #print ingpacks
 out=0
 while reduce(lambda x,y: x and y, [len(p)!=0 for p in ingpacks]):
  while max([ingpacks[i][0][0] for i in range(len(ingpacks))])>min([ingpacks[i][0][1] for i in range(len(ingpacks))]):
   deter=max([packs[0] for packs in ingpacks])
   for i in range(len(ingpacks)):
    while len(ingpacks[i])>0 and ingpacks[i][0][1]<deter[0]: k=ingpacks[i].pop(0)
    if len(ingpacks[i])==0: return out
  kit=[ingpacks[i].pop(0) for i in range(len(ingpacks))]
  #print 'kit',kit
  out+=1
 return out

inp=file('B-large.in','rb+'); out=file('B-large.out','wb+')
for t in range(1,int(inp.readline().strip())+1):
 #print t
 N,P=inp.readline().strip().split(' '); N=int(N); P=int(P)
 serving=[int(n) for n in inp.readline().strip().split(' ')]
 ingpacks=[[int(n) for n in inp.readline().strip().split(' ')] for ing in range(N)]
 out.write('Case #%i: %i\r\n'%(t,sol(N,P,serving,ingpacks)))