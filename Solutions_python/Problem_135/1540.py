"""
doc
"""
from sys import stdin

lines = []

T = int(stdin.readline().split()[0])

for i in range(T):
	row1 = int(stdin.readline().split()[0])
	rows1 = []
	for l in range(4):
		rows1.append(stdin.readline().split())
	row2 = int(stdin.readline().split()[0])
	rows2 = []
	for l in range(4):
		rows2.append(stdin.readline().split())

	auxlist = list(set(rows1[row1-1]) & set(rows2[row2-1]))
	if len(auxlist) > 1:
		result = "Bad magician!"
	elif len(auxlist) < 1:
		result = "Volunteer cheated!"
	else:
		result = str(auxlist[0])
	print "Case #"+str(i+1)+": "+result