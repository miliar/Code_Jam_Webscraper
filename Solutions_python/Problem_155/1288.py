
data = []
answer = []
def load_file(file_name):
	f = open(file_name,"r")
	i = -1
	for line in f:
		i+=1
		if i != 0:
			a = []
			j = 0
			(x,line) = line.split()
			for l in line:
				if l != '\n':
					a.append(int(l))
				j+=1
			data.append(a)

def solve(n):
	cont = 0
	a = 0
	for i in range(0,len(n)):
		if cont < i:
			a += i - cont
			cont += i - cont
		cont += n[i]

	return a

def save_file(file_name):
	f = open(file_name,"w")
	i = 1
	for n in answer:
		f.write("Case #" + str(i) +": "+ str(n)+"\n")
		i += 1






load_file("A-large.in")
for x in range(0,len(data)):
	answer.append(solve(data[x]))

save_file("solve.txt")
