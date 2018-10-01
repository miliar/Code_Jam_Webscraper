t = int(input())
for j in range(1,t+1):
	n = input()
	string1 = input()
	string2 = input()
	uniquestring1 = ''
	uniquestring2 = ''
	count2 = []
	count1 = []
	i = 0	
	index = -1
	while i <= len(string1) - 1:
		if i == 0:
			curr = string1[i]
			uniquestring1 += string1[i]
			index += 1
			count1.append(1)
		else:
			previous = string1[i-1]
			curr = string1[i]
			if previous != curr:
				uniquestring1 += string1[i]
				index += 1
				count1.append(1)
			else:
				count1[index] += 1
		i += 1
	i = 0
	index = -1
	while i <= len(string2) - 1:
		if i == 0:
			curr = string2[i]
			uniquestring2 += string2[i]
			index += 1
			count2.append(1)
		else:
			previous = string2[i-1]
			curr = string2[i]
			if previous != curr:
				uniquestring2 += string2[i]
				index += 1
				count2.append(1)
			else:
				count2[index] += 1
		i += 1
	#print(uniquestring1+'\n'+uniquestring2)
	if uniquestring1 != uniquestring2:
		print("Case #{0}: Fegla Won".format(j))
	else:
		difference = 0
		for i in range(len(uniquestring1)):
			difference += abs(count1[i]-count2[i])
		print("Case #{0}: {1}".format(j, difference))
	uniquestring1 = ''
	uniquestring2 = ''
	count2 = []
	count1 = []