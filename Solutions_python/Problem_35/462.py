def pretty(matrix):
	return '\n'.join([' '.join(map(str,row)) for row in matrix])

def neigh(x,y,w,h):
	res=[]
	if x>0: res.append([x-1,y])
	if y>0: res.append([x,y-1])
	if y<w-1: res.append([x,y+1])
	if x<h-1: res.append([x+1,y])
	return res

f=open('B-small-attempt5.in','r')
out=""
for case in range(int(f.readline())):
	out+="Case #"+str(case+1)+":\n"
	chars="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
	h,w=map(int,f.readline().rsplit())
	if h==1&w==1:
		f.readline()
		out+='a\n'
	else:
		mapa=[map(int,f.readline().rsplit()) for i in range(h)]
		labels=[['' for j in range(w)] for i in range(h)]
		for i in range(len(labels)):
			for j in range(len(labels[i])):
				x,y=i,j
				while True:
					vecinos=neigh(x,y,len(labels[i]),len(labels))
					lower=min(map(lambda pos:mapa[pos[0]][pos[1]],vecinos))
					lowerpos=filter(lambda pos:mapa[pos[0]][pos[1]]==lower,vecinos)[0]
					if labels[lowerpos[0]][lowerpos[1]]!='' and lower<mapa[x][y]:
						labels[i][j]=labels[lowerpos[0]][lowerpos[1]]
						break
					if lower>=mapa[x][y]:
						if labels[x][y]=='': labels[x][y]=chars.pop(0)
						labels[i][j]=labels[x][y]
						break
					else:
						x,y=tuple(lowerpos)
		out+=pretty(labels)+'\n'

outf=open('B-small-attempt5.out','w')
outf.write(out)
