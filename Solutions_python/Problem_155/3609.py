import fileinput
f = fileinput.input("A-small-attempt0.in.txt")
Lnum = f.readline()
wf = open('output.txt', 'w')
for z in range(int(Lnum)):
    line = f.readline()
    shyness_level = line[0]
    clean_line = line.rstrip()
    audience_string = clean_line[2:]
    number_needed = []
    num_to_invite = 0
    standing_up_count = 0
    for i in range(len(audience_string)):
        print "i:", i, "audience_string:", audience_string[i]
        if not int(audience_string[i]) == 0:
            if i == 0:
                standing_up_count += int(audience_string[i])
            elif standing_up_count >= i:
                standing_up_count += int(audience_string[i])
            elif standing_up_count < i:
                number_needed.append([i, audience_string[i]])
        for x in range(len(number_needed)):
            if standing_up_count < number_needed[x][0]:
                new_num_to_invite = (number_needed[x][0] - standing_up_count)
                num_to_invite += new_num_to_invite
                standing_up_count += int(number_needed[x][1]) + new_num_to_invite
    wf.write('Case #'+str(z+1)+': '+str(num_to_invite)+'\n')
wf.close

    