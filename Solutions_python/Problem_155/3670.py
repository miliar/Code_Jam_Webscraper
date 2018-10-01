def people_standing(audience):
	standing = 0
	for shyness_level, number_of_people in enumerate(audience):
		if shyness_level <= standing:
			standing += int(number_of_people)
	return standing

def add_friends(audience):
	audience = list(audience)
	audience[0] = str(int(audience[0]) + 1)
	return "".join(audience)

N = int(raw_input())

for i in xrange(N):
	friends = 0
	retrieved_input = raw_input().split(' ')

	min_standing = int(retrieved_input[0])	
	audience = retrieved_input[1]
	
	if people_standing(audience) < min_standing:
		while people_standing(audience) < min_standing:
			audience = add_friends(audience)
			friends = friends + 1

	print "Case #" + str(i + 1) + ": " + str(friends)



