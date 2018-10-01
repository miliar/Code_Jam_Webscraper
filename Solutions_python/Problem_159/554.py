
def method1(ps):
	total = 0
	for i in range(len(ps)):
		if not i == 0:
			if ps[i-1]>ps[i]:
				total+= ps[i-1] - ps[i]
	return total

def method2(ps):
	maxt = 0
	total = 0
	for i in range(len(ps)):
		if not i == 0:
			maxt =max(maxt,ps[i-1] - ps[i])
	for i in range(len(ps)):
		if not i == len(ps)-1:
			if ps[i] > maxt:
				total += maxt
			else:
				total+=ps[i]
	return total

def read_file(fin,fout):
	f = open(fin)
	i = 0
	fo = open(fout,"w")
	for line in f:
		if not i == 0:
			if i%2 == 0:
				p = line.split()
				ps = []
				for s in p:
					ps.append(int(s))
				t1 = method1(ps)
				t2 = method2(ps)
				write(fo,i/2,t1,t2)
		i+=1


def write(file,i,t1,t2):
	file.write("Case #"+str(i)+": "+str(t1)+" "+str(t2)+"\n")			 


read_file("A-large (1).in","out.txt")