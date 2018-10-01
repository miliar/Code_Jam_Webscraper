myfile = open("A-large.in", "r")
myfile2 = open("output.txt", "w")

case = 0
testcase = int(myfile.readline())

for line in myfile:
	case+=1
	myarr = []
	myline = line.split(" ")
	flipper = int(myline[1])
	counter = 0

	for x in myline[0]:
		if x == "+":
			myarr.append("+")
		else:
			myarr.append("-")

	
	for x in range(len(myarr)-(flipper-1)):

		if myarr[x] == "-":	
			counter+=1
			for y in range(flipper):
				if myarr[x+y] == "-":
					myarr[x+y] = "+"
				else:
					myarr[x+y] = "-"
	
		
	flag = 1
	for x in range(len(myarr)):

		if myarr[x] == "-":
			flag = 0
	if case != 1:
		myfile2.write("\n")		
	
	myfile2.write("Case #")
	myfile2.write(str(case))
	myfile2.write(": ")

	if flag == 1:
		#print myarr
		myfile2.write(str(counter))
	else:
		#print myarr, "impossible"
		myfile2.write("IMPOSSIBLE")

