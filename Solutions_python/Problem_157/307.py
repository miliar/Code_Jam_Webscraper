data = open("C-small-attempt2.in","r")
outfile = open("cj_dijkstra_small.txt","w")


def full_r(x,n):
	#n is number of repeats, x is value.
	if x=="1": return "1"
	if x=="-1":
		if n%2==1: return "-1"
		return "1"
	if x=="i":
		if n%4==1: return "i"
		if n%4==2: return "-1"
		if n%4==3: return "-i"
		if n%4==0: return "1"
	if x=="-i":
		if n%4==1: return "-i"
		if n%4==2: return "-1"
		if n%4==3: return "i"
		if n%4==0: return "1"
	if x=="j":
		if n%4==1: return "j"
		if n%4==2: return "-1"
		if n%4==3: return "-j"
		if n%4==0: return "1"
	if x=="-j":
		if n%4==1: return "-j"
		if n%4==2: return "-1"
		if n%4==3: return "j"
		if n%4==0: return "1"
	if x=="k":
		if n%4==1: return "k"
		if n%4==2: return "-1"
		if n%4==3: return "-k"
		if n%4==0: return "1"
	if x=="-k":
		if n%4==1: return "-k"
		if n%4==2: return "-1"
		if n%4==3: return "k"
		if n%4==0: return "1"

		

def product(x,y):

	#just parses. easy.

	if "-" in x:
		if "-" in y:
			return product(x[1:],y[1:])
		if "-" in product(x[1:],y):
			return product(x[1:],y)[1:]
		else: return "-"+product(x[1:],y)
	if "-" in y:
		if "-" in product(x,y[1:]):
			return product(x,y[1:])[1:]
		else: return "-"+product(x,y[1:])

	###
		
	if x=="1":
		return y
	if x=="i":
		if y=="1": return "i"
		if y=="i": return "-1"
		if y=="j": return "k"
		if y=="k": return "-j"
	if x=="j":
		if y=="1": return "j"
		if y=="i": return "-k"
		if y=="j": return "-1"
		if y=="k": return "i"
	if x=="k":
		if y=="1": return "k"
		if y=="i": return "j"
		if y=="j": return "-i"
		if y=="k": return "-1"
		

t = int(data.readline())

for case in range(0,t):

	info = data.readline()[:-1].split(' ')
	l = int(info[0]) #length
	x = int(info[1]) #number of repeats

	if case!=t-1: string = data.readline()[:-1]
	else: string = data.readline()

	value = 0
	current = "1"
	found_i = 0
	found_j = 0
	while value < l*min(x,4+(x%4)):
		current = product(current,string[value%len(string)])
		if current=="i": found_i=1
		if (current=="k") & (found_i==1):
			found_j=1
		value+=1
		
	outfile.write("Case #" + str(case+1) + ": ")
		
	if (current=="-1") & (found_i==1) & (found_j==1):
		outfile.write("YES")
	else:
		outfile.write("NO")
	if case!=t-1:
		outfile.write("\n")