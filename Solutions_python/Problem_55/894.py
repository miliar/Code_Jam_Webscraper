#!/usr/bin/env python
""" Problem: Theme Park"""
	
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

def groupsPerTrip(G,k):
    #Get groups who can go on each trip
    TRF=0
    NL=G
    index=0
    for i in G:
        if i>(k-TRF):
            break
        TRF=TRF + i
        index+=1
    tmp=NL[:index]
    del NL[:index]
    NL.extend(tmp)
        
    return [TRF,NL]

def main():
	freOpen('C-small-input.in','r','stdin')
	#freOpen('C-large-input.in','r','stdin')
	freOpen('C-small.out','w','stdout')
	#freOpen('C-large.out','w','stdout')
	
	KQ=[]
	T=int(gIn())
	for i in range(T):
            R,k,N=strToIntli(gIn())
            GRPS=strToIntli(gIn())
            #Add all group members to the queue KQ (just a python list)
            KQ=GRPS
            TRF=0
            EUROS=0
            #print k
            for j in range(R):
                #print KQ
                xx=groupsPerTrip(KQ,k)
                EUROS=EUROS+xx[0]
                KQ=xx[1]
                

            print "Case #%d: %d" % (i+1,EUROS)
            
	
if __name__=='__main__':
	main()
	sys.exit(0)
