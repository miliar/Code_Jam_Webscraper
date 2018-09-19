# Google code jam 2015 Qualifying round Problem A

def num_f(lis):
	total = 0
	invite = 0
	for i in range( len(lis) ):
		if total >= i:
			# Enough people stood up, so everyone with shyness i stand
			total += lis[i]
		else:
			# Not enough people stood up - add 
			invite += i - total
			total = i + lis[i]
	return invite

f = open('A-large.in', 'r')

list_num = []
for line in f:
	l = line.split()
	if len(l) == 2:
		list_num.append( l[1] )

for i in range( len(list_num) ):
	l = []
	s = str( list_num[i] )
	for digit in s:
		l.append( int(digit) )
	list_num[i] = l

for i in range( len(list_num) ):
	print "Case #{0}: {1}".format( i + 1, num_f( list_num[i] ) )


