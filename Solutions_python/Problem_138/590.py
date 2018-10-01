
from decimal import *
from collections import deque

t = int(raw_input())

for case in xrange(0,t):
	numOfBlocks = int(raw_input())
	naomi = [ Decimal(a) for a in raw_input().split(' ') ]
	ken = [ Decimal(a) for a in raw_input().split(' ') ]
	naomi.sort()
	ken.sort()
	kenDeque = deque(ken)
	naomiDeque = deque(naomi)
	deceitfulWarWin = 0
	for i in xrange(0,numOfBlocks):
		if kenDeque[0] < naomiDeque[0]:
			deceitfulWarWin = deceitfulWarWin + 1
			kenDeque.popleft()
			naomiDeque.popleft()
		else:
			kenDeque.pop()
			naomiDeque.popleft()
	kenDeque = deque(ken)
	naomiDeque = deque(naomi)
	warWin = 0
	for i in xrange(0,numOfBlocks):
		if kenDeque[-1] < naomiDeque[-1]:
			warWin = warWin + 1
			kenDeque.popleft()
			naomiDeque.pop()
		else:
			kenDeque.pop()
			naomiDeque.pop()
	print( 'Case #{0}: {1} {2}'.format(case+1,deceitfulWarWin,warWin) )
