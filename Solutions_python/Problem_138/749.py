
data = [line.strip().split() for line in open("D-large.in", 'r')]
numtests = int(data.pop(0)[0])
count = 0
while data != []:
	case=data[:3]
	data=data[3:]
	case = [[float(e) for e in el] for el in case]
	naomi = case[1]
	ken = case[2]
	naomi.sort()
	ken.sort()
	naomi2 = naomi[:]
	ken2 = ken[:]
	deceit = 0
	while naomi != []:
		if naomi[-1]>ken[-1]: 
			deceit +=1
			naomi.pop()
			ken.pop()
		else:
			ken.pop()
			naomi.pop(0)
	naomipts = 0
	kenpts = 0
	while kenpts < len(ken2):
		if naomi2[naomipts]>ken2[kenpts]:
			kenpts += 1
			continue
		naomipts += 1
		kenpts += 1
	war = kenpts-naomipts
	count += 1
	print "Case #" + str(count) + ": " + str(deceit) + " " + str(war)



