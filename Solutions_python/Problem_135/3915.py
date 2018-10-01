fp = open("A-small-attempt0.in","r")
tests = fp.readline().strip("\n")
#print(tests)

for i in range(int(tests)):
	numres = 0
	first = int(fp.readline().strip("\n"))
	arr1 = [[],[],[],[]]
	for j in range(4):
		n = fp.readline().strip("\n")
		arr1[j] = n.split(" ")
	#print(arr1)
	second = int(fp.readline().strip("\n"))
	#print("\n\n\n")
	arr2 = [[],[],[],[]]
	for j in range(4):
		n = fp.readline().strip("\n")
		arr2[j] = n.split(" ")
	#print(arr2)
	for elem in arr1[first-1]:
		for elem2 in arr2[second-1]:
			#print("Comparing :",elem,elem2)
			if int(elem) == int(elem2):
				result = int(elem)
				numres += 1
	if numres == 1:
		print("Case #"+str(i+1)+": "+str(result))
	elif numres == 0:
		print("Case #"+str(i+1)+": Volunteer cheated!")
	else:
		print("Case #"+str(i+1)+": Bad magician!")



	