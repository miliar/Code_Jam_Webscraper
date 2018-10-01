def main(x):
  na=inpf.readline().split(' ')
  ke=inpf.readline().split(' ')
  naomi=[]
  ken=[]
  naomic=[]
  kenc=[]
  temp=[]
  war=0
  dec=0
  flag=0
  for i in xrange(int(x)):
     naomi.append(float(na[i]))
     ken.append(float(ke[i]))
  naomi.sort()
  ken.sort()
  for y in xrange(int(x)):
    for i in xrange(len(ken)):
      if naomi[0]<ken[i]:
	temp.append(ken[i])
	flag=1
    if flag==0:
      ken.remove(min(ken))
      del naomi[0]      
      war+=1
    elif flag==1:
      ken.remove(min(temp))
      del naomi[0]
      flag=0
      temp=[]
  for i in xrange(int(x)):
     naomic.append(float(na[i]))
     kenc.append(float(ke[i]))
  naomic.sort()
  kenc.sort()
  flag=0
  temp=[]
  for y in xrange(int(x)):
    for i in xrange(len(naomic)):
      if kenc[0]<naomic[i]:
	temp.append(naomic[i])
	flag=1
    if flag==0:
      naomic.remove(min(naomic))
      del kenc[0]      
      
    elif flag==1:
      naomic.remove(min(temp))
      del kenc[0]
      flag=0
      dec+=1
      temp=[]

  return ("%s %s" %(str(dec),str(war)))
  
if __name__ == '__main__':
	import sys
	inpf=open('1.txt')
	outp=open('output.txt','w')
	N = int(inpf.readline())
	for i in xrange(N):
		inp=inpf.readline().strip()
		res = main(inp)
		outp.write("Case #%d: %s\n" % (i + 1, res))
	outp.close()
	