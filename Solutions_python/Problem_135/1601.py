#!/usr/bin/env python
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	T = int(sys.stdin.readline())
	for t in xrange(T):
		vrow = int(sys.stdin.readline())
		cards1 = []
		for i in xrange(4):
		  row = sys.stdin.readline()
		  if i == vrow - 1:
		    cards1 = map(int, row.split(" "))
		
		vrow = int(sys.stdin.readline())
		cards2 = []
		for i in xrange(4):
		  row = sys.stdin.readline()
		  if i == vrow - 1:
		    cards2 = map(int, row.split(" "))
		
		cards = cards1 + cards2
		uniqueCount = len(set(cards))
		outcome = ""
		if uniqueCount == 8:
		  outcome = "Volunteer cheated!"
		elif uniqueCount <= 6:
		  outcome = "Bad magician!"
		else: # We're good!
		  cards.sort()
		  i = 0
		  while outcome == "":
		    if cards[i] == cards[i + 1]:
		      outcome = str(cards[i])
		    i += 1
		  
		print "Case #%d: %s" % (t + 1, outcome)

if __name__ == "__main__":
	sys.exit(main())

