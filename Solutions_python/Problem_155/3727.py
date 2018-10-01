

def get_min_friends(max_shyness, audience):
	
	stood_up_people=friends_to_invite=0
	if len(audience) == 1:
		return friends_to_invite

	for shy_level,people in enumerate(audience):
		if people != 0 and stood_up_people < shy_level:
			friends_to_invite += shy_level - stood_up_people 
			stood_up_people += people + friends_to_invite
		else:
			stood_up_people += people
	return friends_to_invite



def main():
	for case in range(int(input())):
		splitted_input = raw_input().split(" ")
		max_shyness = int(splitted_input[0])
		audience = map(lambda x: int(x),list(splitted_input[1]))
		print "Case #" + str(case + 1) + ": " + str(get_min_friends(max_shyness, audience))


if __name__ == '__main__':
	main()