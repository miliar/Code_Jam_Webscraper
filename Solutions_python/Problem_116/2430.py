import sys
import collections

def check_status(s):
	# row-wise
	for i in range(0,16,4):
		tmp_dict = collections.Counter(s[i:i+4])
		if (tmp_dict['X'] == 4) or (tmp_dict['X']==3 and tmp_dict['T']==1):
			return 'X won'
		elif (tmp_dict['O'] == 4) or (tmp_dict['O']==3 and tmp_dict['T']==1):
			return 'O won'
	# column-wise
	for i in range(0,4,1):
		tmp_dict = collections.Counter(s[i:16:4])
		#print tmp_dict
		if (tmp_dict['X'] == 4) or (tmp_dict['X']==3 and tmp_dict['T']==1):
			return 'X won'
		elif (tmp_dict['O'] == 4) or (tmp_dict['O']==3 and tmp_dict['T']==1):
			return 'O won'
	# diagonal
	tmp_dict = collections.Counter(s[0:16:5])
	if (tmp_dict['X'] == 4) or (tmp_dict['X']==3 and tmp_dict['T']==1):
		return 'X won'
	elif (tmp_dict['O'] == 4) or (tmp_dict['O']==3 and tmp_dict['T']==1):
		return 'O won'
	tmp_dict = collections.Counter(s[3:14:3])
	if (tmp_dict['X'] == 4) or (tmp_dict['X']==3 and tmp_dict['T']==1):
		return 'X won'
	elif (tmp_dict['O'] == 4) or (tmp_dict['O']==3 and tmp_dict['T']==1):
		return 'O won'
	if '.' in s:
		return 'Game has not completed'
	return 'Draw'

num_cases = int(sys.stdin.next())

for num_case in range(num_cases):
	s=''
	for i in range(4):
		s+=sys.stdin.next().rstrip('\n')
	sys.stdin.next()
	#print s
	print 'Case #%d: %s' % (num_case+1, check_status(s))