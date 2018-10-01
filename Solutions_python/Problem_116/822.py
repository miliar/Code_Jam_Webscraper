
def getWinner(ll):
	nn=0
	for i in xrange(4):
		for j in xrange(4):
			if ll[i][j]=='.':
				nn+=1
		
	for i in xrange(4):
		cnt={'T':0, 'X':0, 'O':0, '.':0}
		for j in xrange(4):
			c=ll[i][j]
			cnt[c]+=1
			if cnt['O'] + cnt['T']==4:
				return (nn, 'O')
			if cnt['X'] + cnt['T']==4:
				return (nn, 'X')
				
	for i in xrange(4):
		cnt={'T':0, 'X':0, 'O':0, '.':0}
		for j in xrange(4):
			c=ll[j][i]
			cnt[c]+=1	
			if cnt['O'] + cnt['T']==4:
				return (nn, 'O')
			if cnt['X'] + cnt['T']==4:
				return (nn, 'X')
				
	cnt={'T':0, 'X':0, 'O':0, '.':0}		
	for i in xrange(4):
		c=ll[i][i]
		cnt[c]+=1
		if cnt['O'] + cnt['T']==4:
			return (nn, 'O')
		if cnt['X'] + cnt['T']==4:
			return (nn, 'X')

	cnt={'T':0, 'X':0, 'O':0, '.':0}		
	for i in xrange(4):
		c=ll[i][3-i]
		cnt[c]+=1
		if cnt['O'] + cnt['T']==4:
			return (nn, 'O')
		if cnt['X'] + cnt['T']==4:
			return (nn, 'X')
		
	return (nn, None)
	
def foo():
	t = input()
	ll=['' for i in xrange(4)]
	for n in xrange(t):
		ll[0]=raw_input()
		ll[1]=raw_input()
		ll[2]=raw_input()
		ll[3]=raw_input()
		if n < t-1:
			na=raw_input()
		
		nn, winner = getWinner(ll)
		if winner!=None:
			print 'Case #%d: %s won' % (n+1, winner)
		elif nn==0:
			print 'Case #%d: %s' % (n+1, 'Draw')
		else:
			print 'Case #%d: %s' % (n+1, 'Game has not completed')
		#return
	
#if __name__ == 'main':
foo()


