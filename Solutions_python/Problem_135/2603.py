#!/usr/bin/python3
# -*- coding: utf-8 -*-

def read (fi):
	row = int(fi.readline())

	for j in range(1, 5):
		if row % j == 0:
			line = fi.readline()
		else:
			fi.readline()
	return line.rstrip("\n").split(" ")
	
def inter (list1, list2):
	res = list()
	for i in list1:
		if i in list2:
			res.append(i)
	return res


		
	

def main(dataIn):
	f = open(dataIn,"r")
	g = open("A.out","a")
	T = int(f.readline())

	for i in range(1, T+1):
		l1= read(f)
		l2= read(f)
		r = inter(l1, l2)

		if len(r) == 0:
			g.write("Case #{}: {}\n".format(i,"Volunteer cheated!"))
		elif len(r) == 1:
			g.write("Case #{}: {}\n".format(i,r[0]))
		else:
			g.write("Case #{}: {}\n".format(i,"Bad magician!"))
		
	f.close()

if __name__ == '__main__':
	main("A-small-attempt0.in")

