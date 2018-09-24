#!/usr/bin/python

import string
from sets import Set

def findOptimalSwitch(engines, query):

	temp = engines.copy()
	switch = 0
	
	for q in query:
		if q in temp:
			temp.remove(q)
			
		if len(temp) == 0:
			switch = switch + 1
			temp = engines.copy()
			temp.remove(q)
					
	return switch

def parseInput():

	N = 0
	
	# open the input file and read in the contents
#	infile = open("A-small.in", "r")
#	infile = open("A-small-attempt0.in", "r")
#	outfile = open("A-small.out", "w")
	infile = open("A-large.in", "r")
	outfile = open("A-large.out", "w")
	
	count = 0
	curCase = 0
	engine = Set()
	query = []
	switches = 0
	for line in infile:
	
		# remove the carriage return
		line = line[0:len(line)-1]
		if count == 0:
			N = int(line)
			print "Number of test cases: " + str(N)
		elif count == 1:
			S = int(line)
			curCase = curCase + 1
			print "Number of search engines: " + str(S)
			switches = 0
		elif count <= S+1:	
			print "Adding search engine: " + line
			engine.add(line)
		elif count == S+2:
			Q = int(line)
			print "Number of queries: " + str(Q)
			
			if Q == 0:
				outfile.write("Case #%d: %d\n" % (curCase, switches))
				count = 0
				
		elif count <= S+2+Q:
			query.append(line)
			
			switches = findOptimalSwitch(engine, query)
			
			if count == S+2+Q:
				# reset the counter to get to next test case
				count = 0	
				engine = Set()
				query = []
				outfile.write("Case #%d: %d\n" % (curCase, switches))
				
		count = count + 1
	
	infile.close()
	outfile.close()

parseInput()