#!/usr/bin/env python

'''

google code jam 2011
round 1b
problem a
RPI

notes:


'''

import sys
import time

fin = sys.stdin
fout = sys.stdout
#fin = open('sample.in', 'r')
#fout = open('sample.out', 'w')

timeit = 1
debugv = 0

def main():
	T = int(fin.readline())
	for case in xrange(1,T+1):
		processCase(case)

def processCase(case):
	N = int(fin.readline())
	schedule = [fin.readline().strip() for row in xrange(N)]
	
	debug("schedule: %s\n" % schedule)
	
	nWins = [float(len([None for x in row if x == '1'])) for row in schedule]
	nGames = [float(len([None for x in row if x != '.'])) for row in schedule]
	
	debug("nWins: %s\n" % nWins)
	debug("nGames: %s\n" % nGames)
	
	WP = [nW / nG for nW, nG in zip(nWins, nGames)]
	debug("WP: %s\n" % WP)
	
	OWP = [
		sum([
			(nWins[j] - int(schedule[j][i])) / (nGames[j] - 1) 
			for j in xrange(N) 
			if schedule[i][j] != '.'
		]) / nGames[i]
		for i in xrange(N)
	]
	debug("OWP: %s\n" % OWP)
	
	OOWP = [
		sum([
			OWP[j]
			for j in xrange(N)
			if schedule[i][j] != '.'
		]) / nGames[i]
		for i in xrange(N)
	]
	debug("OOWP: %s\n" % OOWP)
	
	RPI = [
		0.25 * wp + 0.5 * owp + 0.25 * oowp
		for wp, owp, oowp in zip(WP, OWP, OOWP)
	]
	
	fout.write("Case #%d:\n" % (case))
	for rpi in RPI:
		fout.write("%.12f\n" % (rpi))


def debug(m):
	if debugv:
		sys.stderr.write(m)

startTime = time.clock()
main()
if timeit: sys.stderr.write("completed in %f seconds\n" % (time.clock() - startTime))

