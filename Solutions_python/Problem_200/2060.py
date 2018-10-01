
def tidy_list(l, idx) :
	i = idx
	while i < len(l):
		l[i] = '9' 
		i += 1
	

	i = idx - 1

	if i >= 0:
		if i == 0:
			l[i] = str(int(l[i]) - 1)
			if(l[0] == '0'):
				l.pop(0)
			return
		elif l[i] != l[i-1]:
			l[i] = str(int(l[i]) - 1)
			return
		
		


	
	if i == 0:
		return


	done =False
	while l[i] == l[i-1]:
		# l[i] = str(int(l[i]) - 1)
		l[i] = '9'
		
		# print l, i
		i -= 1
		if i < 1:
			done = True
			l[i] = str(int(l[i]) - 1)
			# print l
			if(l[i] == '0'):
				l.pop(0)
				# print l

			for n in range(len(l)):
				if l[n] == '0':
					l[n] = '9'
				else:
					break
			break

	if done:
		return	
	l[i] = str(int(l[i]) - 1)


T = int(raw_input())


for i in range(T):
	
	num = raw_input()
	seq = list(num)

	idx = 0
	l = len(seq)

	for dig in seq:
		done = False
		if idx > l - 2 :
			break

		if int(seq[idx + 1]) < int(dig):
			
			tidy_list(seq, idx + 1)
			doen = True
			break


		if done == True:
			break
		idx += 1


	print "Case #" + str(i+1) + ": " + ''.join(seq)