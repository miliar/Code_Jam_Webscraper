in1 = '/home/marshynov/Downloads/A-small-attempt0.in'
#in1 = '/home/marshynov/Downloads/a-test.in'
out1 = '/home/marshynov/Downloads/A-small-practice.out'
in_f = open(in1, 'r')
out_f = open(out1, 'w')

def column(matrix, i):
    return [row[i] for row in matrix]

tttt = 'T'
empty_cell = False

def won(lst):
  wnr = None
  #if lst[0]=='.' or lst[1]=='.' or lst[2]=='.' or lst[3]=='.':
  #	global empty_cell  
  #	empty_cell = True
  if (lst[0]==tttt or lst[0]==lst[1]) and (lst[1]==tttt or lst[1]==lst[2]) and (lst[2]==tttt or lst[2]==lst[3] or lst[3]==tttt):
	if lst[0]!='.':
		if lst[0]!='T':
			wnr = lst[0]
		else:
			wnr = lst[1]
  if wnr=='.':
	wnr = None
  return wnr

def dostuff(inx,l1,l2,l3,l4):
	m = [list(l1),list(l2),list(l3),list(l4)]

	finished = False
	winner = None
	for i in range(4):
		res = won(m[i])
		if res is not None:
			finished = True
			winner = res  
	
	if not finished:
		for i in range(4):
			res = won(column(m,i))
			if res is not None:
				finished = True
				winner = res  
	if not finished:
		res = won([list(l1)[0], list(l2)[1], list(l3)[2], list(l4)[3]])
		if res is not None:
			finished = True
			winner = res  

	if not finished:
		res = won([list(l1)[3], list(l2)[2], list(l3)[1], list(l4)[0]])
		if res is not None:
			finished = True
			winner = res  
	
	result = 'Draw'

	if winner is not None:
		result = winner+' '+'won' 
	else:
		#global empty_cell 
		#if empty_cell:
		#	result = 'Game has not completed'
		
		if l1.find('.')!=-1 or l2.find('.')!=-1 or l3.find('.')!=-1 or l4.find('.')!=-1:
			result =  'Game has not completed'
	return 'Case #${0}: {1}'.format(inx,result)


cases = int(in_f.readline())
#print(cases)
for i in range(0,cases):
 l1 = in_f.readline()
 l2 = in_f.readline()
 l3 = in_f.readline()
 l4 = in_f.readline()
 empty_line = in_f.readline()
# nst = ns.split()
 res = dostuff(i+1, l1,l2,l3,l4)
 out_f.write(res+'\n')
 print(res)
