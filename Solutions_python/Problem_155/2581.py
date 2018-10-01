input_file = open('A-large.in', 'r')#get the problem inputs
output_file = open('prob_a_output.txt', 'w')#somewhere to output all them datas
lines = []#all the line in input file
for line in input_file:#get the lines
	if '\n' in line:#if there is a newline
		line = line[0:-1]#remove the newline
	lines.append(line)#add cleaned line to list
def case(string):#this function deals with each case individually
	info = string.split(' ')#we split each case into the important bits
	people = info[1]#this is about the demographic of the crowd's shyness
	standing = 0#this is the number of people currently standing (0 initially)
	friends = 0#this is the number of friends you will need
	for i in range(0,len(people)):#we loop through the demographic
		friends_here = 0#the number of friends needed to get the next group standing
		temp = standing#a temp holder for standing, so we dont change it
		while i > temp:#until i(the shyness level) can be satisfied;
			friends_here += 1#we keep adding friends until they stand
			temp = standing + friends_here#update temp accordingly
		standing += int(people[i]) + friends_here#we have enough friends for that shyness, so update the number standing
		friends += friends_here#update number of friends total
	return friends#return friends needed as integer
for i in range(1,len(lines)):#loop through all the cases
	string = "Case #" + str(i) + ": " + str(case(lines[i])) + '\n'#create the string
	output_file.write(string)#write to the output file