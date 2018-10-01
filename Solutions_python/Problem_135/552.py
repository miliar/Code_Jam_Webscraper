#!/bin/python3
num_cases = int(input())
for casenum in range(1, num_cases+1):
	# r, t = [int(z) for z in input().split()]
	ind1 = int(input())	
	square1 = []#index row, col
	for i in range(4):
		square1.append([int(z) for z in input().split()]) 

	ind2 = int(input())
	square2 = []#index row, col
	for i in range(4):
		square2.append([int(z) for z in input().split()]) 

	result, total = 0, 0
	for num in square1[ind1 - 1]: #look at indexed row
		if num in square2[ind2 - 1]:
			result = num
			total += 1

	if total == 1:
		print ("Case #{0}: {1}".format(casenum, result))
	elif total > 1:
		print ("Case #{0}: Bad magician!".format(casenum))
	else:
		print ("Case #{0}: Volunteer cheated!".format(casenum))