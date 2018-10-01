#!/usr/bin/env python
""" Problem: Alien language"""
	
__author__="Osure Ronald a.k.a sureronald"

"""
Sureronald's own utilities
"""
import sys
import heapq as h

def gIn():
	"""Get user input"""
	return raw_input()
	
	
def freOpen(file,mode,state):
	"""(Get input from)/(Write output to) file"""
	try:
		fPtr=open(file,mode)
	except IOError:
		print "Could not open file!!"
		sys.exit(127)
		
	if state=='stdin':
		sys.stdin=fPtr
	else:
		sys.stdout=fPtr
	
def strToIntli(s):
	"""Explode a string to list and convert contents to int"""
	li=s.split(' ')
	for i in range(len(li)):
		li[i]=int(li[i])
	return li
	
def strToDoubleli(s):
	"""Explode a string to list and convert contents to double"""
	li=s.split(' ')
	for i in range(len(li)):
		li[i]=int(li[i])
	return li
#End sureronald's own utilities

def main():
	#freOpen('small.in','r','stdin')
	freOpen('large.in','r','stdin')
	#freOpen('small.out','w','stdout')
	freOpen('large.out','w','stdout')
	L,D,N=strToIntli(gIn())
	al=[]
	for j in range(D):
		al.append(gIn())
	for i in range(N):
		s=gIn()
		v=[]
		b=False
		g=''
		q=0
		for f in s:
			
			if f.isalpha() and b==False:
				v.append(f)
				
			if f=='(':
				b=True
				
			if f.isalpha() and b==True:
				g+=f
			try:
				if s[q+1]==')':
					v.append(g)
					g=''
					b=False
			except IndexError:
				pass
			q+=1
			
		
		sm=v	
		#print "len sm is %d" % len(sm)
		cnt=0
		for p in al:
			state=0
			c=0
			for x in sm:
				if p[c] in x:
					state+=1
				else:
					break
				c+=1
			if state==L:
				cnt+=1
				state=0

		print "Case #%d: %d" % ((i+1),cnt)
	
if __name__=='__main__':
	main()
	sys.exit(0)
