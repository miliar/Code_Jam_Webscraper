def calculate_values(value,p,surprise):
	base = value / 3
	mod = value % 3
	if mod == 0:
		if base >= p:
			return True,surprise
		elif  (base > 0) & (base + 1 >= p) & (surprise > 0):
			surprise -= 1
			return True,surprise	 
	elif mod == 1:
		print "Modulo 1 con valor %d p %d base %d"%(value,p,base)
		if (base >= p) | (base + 1) >= p:
			return True,surprise
		elif (surprise > 0) & (base + 1) >= p:
			surprise -=1
			return True,surprise
	else:
		if (base >= p) | (base + 1) >=p:
			return True,surprise
		elif (surprise > 0) & (base + 2 >= p):
			surprise -=1
			return True,surprise
	return False,surprise

def calculate_triplet(n,p,surprise): 
	result = 0
	for value in n:
		out,surprise =calculate_values(int(value),p,surprise)
		print "Valore: ", value
		print "Salida ",out
		if out:
			result +=1
	return result
	
				

file = open("B-large.in", "r+")
ofile = open("output.txt","w+")
count = file.readline()
number = 1
for line in file:
	values = line.split()
	googlers = int(values[0])
	surprise = int(values[1])
	p = int(values[2])
	N = []
	for i in range(googlers):
		N.append(values[3+i])
	result = calculate_triplet(N,p,surprise)
	ofile.write("Case #"+str(number)+": "+str(result) +"\n")
	number +=1