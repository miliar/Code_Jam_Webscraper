def maxnotsurprising(totalscore): return [totalscore/3, totalscore/3+1, totalscore/3+1][totalscore%3]
def maxsurprising(totalscore): return [maxnotsurprising(totalscore),[totalscore/3+1, totalscore/3+2, totalscore/3+2][totalscore%3]][totalscore>1]

def answer(scores, p, S):
 nsurp=filter((lambda x: maxnotsurprising(x)>=p), scores)
 surp=filter((lambda x: maxsurprising(x)>=p), scores)
 return len(nsurp) + min(len(surp)-len(nsurp), S)
 

input=[x.strip() for x in file('B-small-attempt0.in','rb+').read().split('\n')[1:]]
output=file('B-small-attempt0.out','wb+')
for l in range(len(input)):
 line=[int(x.strip()) for x in input[l].split(' ')]
 output.write('Case #'+str(l+1)+': '+str(answer(line[3:], line[2], line[1]))+'\n')