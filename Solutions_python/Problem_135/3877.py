tc = int(raw_input())
w = 1
while(tc):
	
	l1 = []
	l2 = []
	cnt = 0
	magic_trick1 = int(raw_input())
	for j in range(4):
		list = raw_input()
		list = list.split()
		l1 = l1 + list
	
	magic_trick2  = int(raw_input())
	for j in range(4):
		list = raw_input()
		list = list.split()
		l2 = l2 +list
	
	tc = tc -1	
	idx1= (magic_trick1-1)*4
	
	idx2 = (magic_trick2-1)*4
	
	list1= l1[idx1 : idx1+4]
	list2 = l2[idx2: idx2+ 4]
	answer = []
	for value in list1:
		if value in list2:
			answer.append(value)

	for u in answer:
		cnt = cnt +1
	if cnt == 1:
		print 'Case #%d: %s' % (w, answer[0])
	elif cnt == 0:	
		print 'Case #%d: %s' % (w,'Volunteer cheated!')
	else:
		print 'Case #%d: %s' % (w,'Bad magician!')
	w = w + 1
	