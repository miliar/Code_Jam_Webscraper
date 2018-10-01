import math

f = open('ds')
g = open('output', 'w')
lines = f.readline()
lines = int(lines)



for case in range(0, lines):
	clock = 0
	rb_o = 1;
	rb_b = 1;
	orange = []
	blue = []
	order = []
	ln = f.readline()
	cmds_len = ln[0:4].split()[0]
	cmd = ln.split()
	cmd.pop(0)
	#print(cmd)
	for i in range(0,int(cmds_len)):
		if(cmd.pop(0) == 'O'):
			orange.append(cmd.pop(0))
			order.append('O')
		else:
			blue.append(cmd.pop(0))
			order.append('B')

	#raw_input()
	i = 0
	while(order):
		pressed = False

		if(orange):
			if(rb_o == int(orange[0]) and not pressed):
				if(order[0] == 'O'):
					orange.pop(0)
					order.pop(0)
					pressed = True
			elif(rb_o < int(orange[0])):
				rb_o+=1
				#print('orange {0} / {1}'.format(rb_o,orange[0]))
			elif(rb_o > int(orange[0])):
				rb_o-=1
				#print('orange {0} / {1}'.format(rb_o,orange[0]))
		if(blue):
			if(rb_b == int(blue[0]) and not pressed):
				if(order[0] == 'B'):
					blue.pop(0)
					order.pop(0)
			elif(rb_b < int(blue[0])):
				rb_b+=1
				#print('orange {0} / {1}'.format(rb_b,blue[0]))
			elif(rb_b > int(blue[0])):
				rb_b-=1
				#print('orange {0} / {1}'.format(rb_b,blue[0]))
		i+=1
	g.write("Case #{0}: {1} \n".format(case + 1, i))
