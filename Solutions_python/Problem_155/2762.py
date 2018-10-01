#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
	maximumShy = int(cipher.split(' ')[0])
	audienceShyness = cipher.split(' ')[1]
	standingAudienceCount = 0
	additionalFriends = 0
	for shyPeople in xrange(0, maximumShy + 1):
		if (int(audienceShyness[shyPeople]) != 0 and shyPeople > standingAudienceCount + additionalFriends):
			additionalFriends = shyPeople - standingAudienceCount
		standingAudienceCount = standingAudienceCount + int(audienceShyness[shyPeople])
	return additionalFriends

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
