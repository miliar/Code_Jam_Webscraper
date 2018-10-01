#!/usr/bin/python
import string
import sys, getopt
def study_candidates(can1,can2):
	cheated=True
	results=[]
	for s in can2:
		if s in can1:
			results.append(s)

	if len(results)==1:
		return results[0]
	if len(results)==0:
		return 'Volunteer cheated!'
	
	return 'Bad magician!'

	

def main(datain,dataout):
	fin = open(datain, "r+")
	lines = fin.readlines()
	fin.close()
	fout=open(dataout,"w")
	cases=int(lines[0])
	position=1
	candidates=[]
	candidates_2=[]
	result=''
	for i in range(1,cases+1):
		selecction=int(lines[position]);
		numbers=string.split(lines[position+selecction],' ')
		for n in numbers:
			candidates.append(int(n))
		position+=5
		selecction_2=int(lines[position])
		numbers_2=string.split(lines[position+selecction_2],' ')
		for m in numbers_2:
			candidates_2.append(int(m))
		position+=5
		result="Case #%d: %s \n" % (i,study_candidates(candidates,candidates_2))
		fout.write(result)
		candidates=[]
		candidates_2=[]

 
	
	fout.close()

def inputfile(argv):
	if(len(argv)==2):
		inputfile = str(sys.argv[1])
		outputfile = str(sys.argv[2])
		main(inputfile,outputfile)
	else:
		print 'PLEASE !! Usage is : python magicTrick.py <inputfile> <outputfile>'
     
	

if __name__ == "__main__":
   inputfile(sys.argv[1:])

