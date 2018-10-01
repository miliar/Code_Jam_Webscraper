#!/usr/bin/python

import sys
import copy

def war(naomi, ken):
	n = copy.copy(naomi)
	k = copy.copy(ken)
	nscore = kscore = 0
	while len(n) > 0:
		nb = n.pop()
		kpos = [x for x in k if x > nb]
		if len(kpos)>0:
			k.remove(kpos[0])
			kscore += 1
		else:
			k.remove(k[0])
			nscore += 1
	return nscore

def done(n, k):
	if len(n)==0:
		return True
	return len([i for i in range(0,len(n)) if n[len(n)-1-i]<k[i] ]) == 0

def deceit(naomi, ken):
	n = copy.copy(naomi)
	k = copy.copy(ken)
	# n plays lightest, k plays heaviest until smallest n > heaviest k.  n wins the rest.
	n.sort()
	n.reverse()
	k.sort()
	while done(n,k)==False:
		nb = n.pop()
		kb = k.pop()
	return len(n)

def eval(naomi, ken):
	return (deceit(naomi, ken), war(naomi, ken))

def getInput():
	N = int(sys.stdin.readline())
	naomi = [float(x) for x in sys.stdin.readline().split()]
	ken = [float(x) for x in sys.stdin.readline().split()]
	naomi.sort()
	ken.sort()
	return (naomi, ken)

T = int(sys.stdin.readline())
for i in range(1,T+1):
	(naomi, ken) = getInput()
	(x,y) = eval(naomi, ken)
	print 'Case #'+str(i)+':', x, y
