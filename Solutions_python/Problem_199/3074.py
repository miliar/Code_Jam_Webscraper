import sys
fName=sys.argv[1]
with open(fName) as f:
    content = f.readlines()
content = [x.strip() for x in content]

out=open(sys.argv[2],'w+')

for i in range(1,int(content[0])+1):
	out.write('Case #%d: '%i)
	values=content[i].split()
	flipper=list(values[0])
	tl=int(values[1])
	a=set([])
	counter=0
	possible=True
	while('-' in flipper):
		i=flipper.index('-')
		if len(flipper)-i<tl:
			possible=False
			break
		else:
			some=i
			for j in range(i,some+tl):
				if flipper[j]=='+':
					flipper[j]='-'
				else:
					flipper[j]='+'
			counter+=1
			string="".join(flipper)
			#out.write(string)
			#out.write('\n')
			if string in a:
				possible=False
				break
			else:
				a.add(string)
	if possible:
		out.write(str(counter))
		out.write('\n')
	else:
		#out.write('\n')
		#out.writ("".join(flipper))
		out.write("IMPOSSIBLE")
		out.write('\n')
out.close()