lines = [line.rstrip('\n') for line in open('A-small-attempt2.in')]

T = int(lines[0])

f = open('pancake.out', 'w')

for k in range(1, T+1):
	l = lines[k]
	pancakes = list(l[0:l.index(' ')])
	flipper = int(l[l.index(' ')+1:])

	length = len(pancakes)
	max_len = length-flipper+1
	checked = []
	ans = ''
	found = False
	p_list = [pancakes]
	d_list = [0]
	checked.append(''.join(pancakes))
	if '-' not in pancakes:
		ans = 0
		found = True
	while(len(p_list) is not 0 and not found):
		pancakes = p_list.pop(0)
		flips = d_list.pop(0)
		#print(''.join(pancakes))
		for i in range(0, max_len):
			copy_pancakes = pancakes[:]
			for j in range(i, i+flipper):
				if (copy_pancakes[j] is '-'):
					copy_pancakes[j] = '+'
				else:
					copy_pancakes[j] = '-'
			if '-' not in copy_pancakes:
				ans = flips+1
				found = True
			if ''.join(copy_pancakes) not in checked:
				p_list.append(copy_pancakes)
				d_list.append(flips+1)
				checked.append(''.join(copy_pancakes))

	if not found:
		ans = "IMPOSSIBLE"
	if (k < T):
		f.write("Case #" + str(k) + ": " + str(ans) + "\n");
	else:
		f.write("Case #" + str(k) + ": " + str(ans));