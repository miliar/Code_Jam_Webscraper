# -*-coding:Utf-8 -*

import sys

# Parse args
with open("A-large.in") as f:
	arg = f.readlines()

T = int(arg[0])
case = [0 for x in range(int(T))]
for ct in range(T):
	case[ct] = map(int, arg[1+ct].split()[1])
	
f = open('A.out','w')

# Compute each case
for ct in range(int(T)):
	# Print data in memory
	# print "*************** case number " + str(ct)
	# print "list : " + str(case[ct])

	# Solve !
	ovation = case[ct][0]
	addedFriends = 0
	del case[ct][0]
	# Iterate over each shyness level
	for shyness, number in enumerate(case[ct]):
		shyness += 1
		# print str(number) + " people shy-level " + str(shyness)
		if(ovation < shyness):
			# Oh no ! Our friend need helps !
			# print str(shyness - ovation) +  " friends needed !" 
			addedFriends += shyness - ovation
			ovation = shyness
		ovation += number

	# print "added friends : " + str(addedFriends)
	
	# Write output
	f.write ("Case #" + str(ct+1) + ": " + str(addedFriends) + "\n")

f.close()
