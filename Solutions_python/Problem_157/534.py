#!/usr/bin/env python 
import sys
import os
#'''
dbg = lambda x: sys.stdout.write(str(x)+'\n')
dbg = lambda x: None
#'''
Q = ['1','i','j','k','-1','-i','-j','-k']
tailing= {	       # [ '1', 'i', 'j', 'k' ] 
	  '1':dict(zip(Q,[ '1', 'i', 'j', 'k'])), #
	  'i':dict(zip(Q,[ 'i','-1', 'k','-j'])), #
	  'j':dict(zip(Q,[ 'j','-k','-1', 'i'])), #
	  'k':dict(zip(Q,[ 'k', 'j','-i','-1'])), #
	  #
	 '-1':dict(zip(Q,['-1','-i','-j','-k'])), #
	 '-i':dict(zip(Q,['-i', '1','-k', 'j'])), #
	 '-j':dict(zip(Q,['-j', 'k', '1','-i'])), #
	 '-k':dict(zip(Q,['-k','-j', 'i', '1'])), #
}
decap= {		   # [ '1', 'i', 'j', 'k' ] 
	  '1':dict(zip(Q,[ '1','-i','-j','-k'])), #
	  'i':dict(zip(Q,[ 'i', '1', 'k','-j'])), #
	  'j':dict(zip(Q,[ 'j','-k', '1', 'i'])), #
	  'k':dict(zip(Q,[ 'k', 'j','-i', '1'])), #
	  #
	 '-1':dict(zip(Q,['-1', 'i', 'j', 'k'])), #
	 '-i':dict(zip(Q,['-i','-1','-k', 'j'])), #
	 '-j':dict(zip(Q,['-j', 'k','-1','-i'])), #
	 '-k':dict(zip(Q,['-k','-j', 'i','-1'])), #
}

def hat_tail_test(s,val_hat='i',val_tail='i'):
	q= False
	dbg( ('val_hat,val_tail=',(val_hat,val_tail)) ) 
	hat = '1'
	tail = '1'
	for ch in s:
		tail = tailing[tail][ch]
	L = []
	T = [] 
	for i,ch in enumerate(s):
#		dbg( ("ch= '%s'"%ch) ) #,'------') )
#		hat_old= hat
#		tail_old= tail 
		hat= tailing[hat][ch]
		tail= decap[tail][ch]
#		dbg( ('hat:',hat_old,'->',hat) )
#		dbg( ('tail:',tail_old,'->',tail) )
		if hat == val_hat and tail == val_tail:
			L.append(i)
	dbg('')
	return L	
def torso_test(s,I,K):
	for k in K:
		for i in I:
			if i>=k:
				continue
			torso='1'
			for ch in s[i+1:k+1]:
#				torso_old= torso
				torso= tailing[torso][ch]
#				dbg( ("ch= '%s'"%ch) ) #,'------') )
#				dbg( ('torso:',torso_old,'->',torso) )
			if torso == 'j':
				#Z.append( (i,k) )
				#return True
				return (i,k)
	return False

def solve(L,X,C):
	dbg('')
	
	dbg( ('(L,X,C):',(L,X,(len(C),C[:20]))) )
	s = C*X
	dbg( ('s:',(len(s),s[:80]+'...')) )
	I = ( hat_tail_test(s,'i','i') )
	dbg( ('I=',(len(I),I[:5])) )
	K = ( hat_tail_test(s,'k','k') )
	dbg( ('K=',(len(K),K[:5])) )
	
	q= torso_test(s,I,K)
	dbg( ('q:',(q)) )
	y = bool(q)
	return y;

def main():
	if '-t' in sys.argv:
		os.system('cat ./input | ./main.py')
		sys.exit()

	T = int(input())
	for i in range(1,T+1):
		L,X = map(int,sys.stdin.readline().split(' '))
		C = sys.stdin.readline().strip() 
		y = solve(L,X,C)
		print 'Case #%d: %s'%(i,['NO','YES'][int(y)])
	return 0

if __name__=='__main__':
	sys.exit(main())
