#!/usr/bin/python

import csv
import itertools as it


maxShy = int(0)
plist = []
cases = []

class PatronGroup:
	def __init__(self,shyLevel,totalPatrons):
		self.shyLevel = int(shyLevel)
		self.totalPatrons = int(totalPatrons)
		self.standing = False
	def stand(self,standingNum):
		if self.totalPatrons == 0:
			return 0
		else:
			if self.shyLevel == 0:
				self.standing = True
				return 0
			elif standingNum >= self.shyLevel:
				self.standing == True
				return 0
			else:
				numFriends = self.shyLevel - standingNum
				self.Standing = True
				return numFriends 
	def getTotalStanding(self):
		return self.totalPatrons

class Case:
	counts = 0
	
	def __init__(self,max,patronGroupList):
		self.max = max
		self.patronGroupList = patronGroupList
		self.invites = int(0)
		self.standing = int(0)
		Case.counts += 1
		self.caseNum = Case.counts
		self.lowest = int(600)
	def printInfo(self):
		print(self.caseNum)
		for p in self.patronGroupList:
			print("SHY LEVEL: " + str(p.shyLevel))
			print ("TOTAL " + str(p.totalPatrons))
	def solve(self):
		combos = it.permutations(range (0,len(self.patronGroupList)), len(self.patronGroupList))
		for c in combos:
			"print(c)"
			inv = int(0)
			std = int(0)
			for x in c:
				inv += int(self.patronGroupList[x].stand(std))
				std += int(self.patronGroupList[x].getTotalStanding() + self.patronGroupList[x].stand(std))
			if inv < self.lowest:
				self.lowest = inv
		"print(str(self.lowest))"	
		return("Case #"+ str(self.caseNum) +": "+ str(self.lowest))

				
	
def readTxt(fi):
	global maxShy
	global plist
	with open(fi,'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=' ')
		lineCount = 0
		firstRowRead = False
		for row in reader:
			if firstRowRead is False:
				caseTotal = row[0]
				firstRowRead = True
				print 
			else:
				lineCount += 1
				if lineCount == 1:
					maxShy = row[0]
					p = row[1]
					for x in range(len(p)):
						pgroup = PatronGroup(x,p[x])
						plist.append(pgroup)
					case = Case(maxShy,plist)
					cases.append(case)
					maxShy = 0
					plist = []
					lineCount = 0

						
						
					

				
								

readTxt("A-small-attempt1.in")
"""readTxt("sample.txt")"""
f = open('Answer.out','w')
for c in cases:
	print(c.solve())
	f.write(c.solve())
	f.write("\n")
f.close()



