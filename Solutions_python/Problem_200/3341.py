import sys
fName=sys.argv[1]
with open(fName) as f:
    content = f.readlines()
content = [x.strip() for x in content]

out=open(sys.argv[2],'w+')

def check(xa):
	j=0
	fault=False
	xa=list(xa)
	for i in range(1,len(xa)):
		if int(xa[j])>int(xa[i]):
			fault=True
			break
		j+=1
	if fault:
		i=0
		while(xa[i]!=xa[j]):
			i+=1
		if i==0 and xa[i]=='1':
			return "9"*(len(xa)-1)
		else:
			xa[i]=str(int(xa[i])-1)
			i+=1
			while(i<len(xa)):
				xa[i]='9'
				i+=1
			return "".join(xa)
	else:
		return "".join(xa)
for i in range(1,int(content[0])+1):
	out.write('Case #%d: '%i)
	length=len(content[i].strip())
	value=int(content[i].strip())
	string=content[i].strip()
	if length==1:
		out.write(string)
		out.write('\n')
	else:
		out.write(check(string))
		out.write('\n')
out.close()