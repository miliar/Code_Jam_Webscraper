
f_in = open('A-large.in')
my_input = f_in.readlines()
f_in.close()

line_count = int( my_input.pop(0) )



cases = []

while my_input:
	line = my_input.pop(0)
	parts = line.split()
	s_max, audience = parts
	s_max = int(s_max)
	audience = [ int(c) for c in audience ]
	#print s_max, audience
	if len(audience)-1 > s_max: raise Exception()
	cases.append( audience )


f_out = open('output.txt', 'w')

for case_num, case in enumerate(cases):
	people_to_invite = 0
	my_sum = 0
	for s_level, s_count in enumerate(case):
		if s_level > my_sum: this_people_to_invite = s_level - my_sum
		else: this_people_to_invite = 0
		my_sum += s_count + this_people_to_invite
		people_to_invite += this_people_to_invite
	toWrite = 'Case #%d: %d\n' % (case_num+1, people_to_invite)
	f_out.write( toWrite )

f_out.close()
	
