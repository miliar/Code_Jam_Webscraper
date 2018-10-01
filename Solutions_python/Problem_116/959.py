def score(game):
	#rows
	p = 0
	i=j=0
	last = ''
	while i<4:
		o=x=0
		while j<4:
			s = game[i][j]
			if s=='.':
				p=1
				break
			elif s =='X':
				x=x+1
				j=j+1
			elif s =='O':
				o=o+1
				j=j+1	
			elif s=='T':
				x=x+1
				o=o+1
				j=j+1
		i=i+1
		j=0
		if(o==4):
			return 'O won'
		if(x==4):
			return 'X won'

	#columns
	i=0
	while i<4:
		x=o=0
		while j<4:
			s = game[j][i]
			if s=='.':
				p=1
				break
			elif s =='X':
				x=x+1
				j=j+1
			elif s =='O':
				o=o+1
				j=j+1	
			elif s=='T':
				x=x+1
				o=o+1
				j=j+1
		i=i+1
		j=0
		if(o==4):
			return 'O won'
		if(x==4):
			return 'X won'

	#diagonal 1
	x=o=0
	for i in range(0,4):
		s = game[i][i]
		if s=='.':
			break
		elif s =='X':
			x=x+1
		elif s =='O':
			o=o+1	
		elif s=='T':
			x=x+1
			o=o+1
	if(o==4):
		return 'O won'
	if(x==4):
		return 'X won'

	#diagonal 1
	x=o=0
	for i in range(0,4):
		s = game[i][3-i]
		if s=='.':
			break
		elif s =='X':
			x=x+1
		elif s =='O':
			o=o+1	
		elif s=='T':
			x=x+1
			o=o+1
	if(o==4):
		return 'O won'
	if(x==4):
		return 'X won'	

	if p>0:
		return 'Game has not completed'
	else:
		return 'Draw'

				



## Main
f = open('A-large.in')
## Read the first line 
line = f.readline()
n = int(line)
line = f.readline()

game = [[0 for col in range(4)] for row in range(4)]

k=0
while k<n:
	i=0
	while i<4:
		j=0
		for letter in line:
			if j== 4:
				break
			game[i][j]=letter
			j=j+1
		line = f.readline()
		i=i+1
	print 'Case #'+ str(k+1) + ': ' + score(game)
	line = f.readline()
	k=k+1
f.close()


