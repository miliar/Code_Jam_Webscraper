def find(c,f,x):
	my_rate = float(2)
	curr = float(0)
	_min = float(0)

	farm = (c / my_rate)
	finish = (x / my_rate)

	if(finish < farm):
		return finish
	curr = farm
	_min = finish 
	my_rate += f
	while(True):
		attempt = curr + (x / my_rate)
		if(_min < attempt):
			return _min
		else:
			_min = attempt
		curr += (c / my_rate)
		my_rate += f

######

f = open('cookie.in')
r = f.readlines()
f.close()

num_cases = int(r[0].strip())

curr = 1
answers = []
while (num_cases != 0):
	line = r[curr].strip().split()
	curr+=1
	c = float(line[0])
	f = float(line[1])
	x = float(line[2])
	answers.append(find(c,f,x))
	num_cases -= 1
#### END WHILE

case = 1
f = open('cookie.out','w')
for answer in answers:
	f.write("Case #%d: %.7f\n" % (case,answer))
	case+=1
f.close()