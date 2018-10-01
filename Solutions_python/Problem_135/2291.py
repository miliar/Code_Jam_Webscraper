import os
import sys

def proc(cands, mat, row):
	res = []
	for i in mat[row-1]:
		if i in cands:
			res.append(i)
	return res
def readMat(ints, pt):
	mat = []
	for j in range(0,4):
		arr =[]
		for k in range(0,4):
			arr.append(ints[pt])
			pt += 1
		mat.append(arr)
	return mat, pt
if __name__ == "__main__":
	f = open('input.txt')
	numCases = -1

	ints = []
	for line in f:
		for str in line.strip().split():
			ints.append(int(str))
	pt = 0
	numCases = ints[pt]
	pt += 1
	
	for i in range(0, numCases):
		cands = []
		for j in range(0, 16):
			cands.append(j+1)
		row = ints[pt]
		pt+=1
		mat, pt = readMat(ints, pt)
		cands = proc(cands, mat, row)
		#print cands
		row = ints[pt]
		pt += 1
		mat, pt = readMat(ints, pt)
		cands = proc(cands, mat, row)
		#print cands
		res = "Case #{0}: ".format(i+1)
		if len(cands) == 0:
			res +=  'Volunteer cheated!'
		elif len(cands) == 1:
			res += "{0}".format(cands[0])
		else :
			res += 'Bad magician!'
		print res
			
