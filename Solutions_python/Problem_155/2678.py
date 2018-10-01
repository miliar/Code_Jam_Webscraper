def call_friends(input_str):
    max_shyness = int( input_str.strip().split()[0] )
    num_people = input_str.strip().split()[1]
    standing_person = 0
    num_friends_to_call = 0
    for shy_level in range(max_shyness+1):
        if standing_person >= shy_level:
            standing_person += int( num_people[shy_level] )
        else:
            num_friends_to_call += shy_level - standing_person
            standing_person += shy_level - standing_person 
            standing_person += int( num_people[shy_level] )

        if standing_person >= max_shyness:
            break

    return num_friends_to_call


testcase = int(raw_input().strip())
for num_case in range(testcase):
    print 'Case #{0}: {1}'.format(num_case+1, call_friends(raw_input().strip()))
