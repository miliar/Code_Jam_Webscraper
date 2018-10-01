#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import copy


def pictureToString(picture):
	
	output = ""
	
	for row in range(len(picture)):
		for elem in range(len(picture[row])):
			output += picture[row][elem]
		
		if row < (len(picture) - 1):
			output += "\n"
	
	return output

def hasBlues(picture):
	
	for row in picture:
		for elem in row:
			if elem == '#':
				return True
	
	return False
	

def changePicture(picture,i,j):
	if (i+1) >= len(picture) or (j+1) >= len(picture[i]): return picture

	if (picture[i][j] == '#' and picture[i+1][j] == '#' and picture[i+1][j+1] == '#' and picture[i][j+1] == '#'):
		picture[i][j] = '/'
		picture[i][j+1] = "\\"
		picture[i+1][j] = '\\'
		picture[i+1][j+1] = '/'
	
	return picture


def processRow(picture):
	pcopy = copy.deepcopy(picture)
	
	for i in range(len(pcopy)):
		for j in range(len(pcopy[i])):
			if pcopy[i][j] == '#':
				pcopy = changePicture(picture,i,j)
				
	
	if(hasBlues(pcopy)):
		return "Impossible"
	else:
		return pictureToString(pcopy)
	


def main():
	infile = open('A-large.txt','r')
	outfile = open('A-large-answer.txt','w')
	
	num_tests = int(infile.readline())

	for x in range(num_tests):
		nums = infile.readline().split()
		nums = [int(n.strip()) for n in nums]
		rows = nums[0]
		cols = nums[1]
		
		picture = []
		
		for y in range(rows):
			row = list(infile.readline().strip())
			picture.append(row)
		
		answer = processRow(picture)
		
		print "Case #"+str(x+1)+":\n",answer
		outfile.write("Case #"+str(x+1)+": \n"+str(answer)+"\n")

	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

