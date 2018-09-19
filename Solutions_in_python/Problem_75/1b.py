import sys

n = 0

for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	
	word = line.split()
	
	C = int(word[0])
	D = int(word[1+C])
	N = int(word[2+C+D])
	
	comstr = []
	oppstr = []
	
	for i in range(C):
		comstr += [word[1+i]]
	for i in range(D):
		oppstr += [word[2+C+i]]
	
	bestr = word[3+C+D]
	afstr = ""
	for i in range(N):
		afstr += bestr[i]
		aflen = len(afstr)
		if aflen < 2:
			continue
		for x in range(C):
			if len(afstr) < 2:
				break
			if (afstr[-1] == comstr[x][0] and afstr[-2] == comstr[x][1]) or (afstr[-1] == comstr[x][1] and afstr[-2] == comstr[x][0]):
				afstr = afstr[:-2]
				afstr += comstr[x][2]
		for x in range(D):
			if len(afstr) < 2:
				break
			if afstr[-1] == oppstr[x][0]:
				for y in range(len(afstr)-1):
					if afstr[y] == oppstr[x][1]:
						afstr = ""
						break
			elif afstr[-1] == oppstr[x][1]:
				for y in range(len(afstr)-1):
					if afstr[y] == oppstr[x][0]:
						afstr = ""
						break
	outstr = "["
	for i in range(len(afstr)):
		outstr+= afstr[i]
		if i != (len(afstr) -1):
			outstr+=", "
	outstr += "]"
		
	print "Case #" + str(n) + ": " + outstr
	n += 1
