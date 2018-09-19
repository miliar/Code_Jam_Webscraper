input_file = open('A-small-attempt1.in')

t = int(input_file.next().rstrip('\n'))  # The first line of the input gives the number of test cases, T.

test_cases = []
for x in range(t):  # T test cases follow.
    audience = input_file.next().rstrip('\n')  # Each consists of one line with D, the number of diners with non-empty plates,
    max_shyness = int(audience[0])
    shynesses_text = audience[2:max_shyness+3]
    shynesses = []
    for shyness in shynesses_text:
        shynesses.append(int(shyness))

    friends_to_invite = 0
    people_clapping = 0
    for required_people in xrange(len(shynesses)):
        if required_people > people_clapping:
            friends_to_invite += required_people - people_clapping
            people_clapping = required_people
        people_clapping += shynesses[required_people]

    print('Case #'+str(x+1)+': ' + str(friends_to_invite))