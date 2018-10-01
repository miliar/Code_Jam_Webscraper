import numpy as np
import pandas as pd

out = []
df = pd.read_csv('B-small-attempt0.in',header=None,index_col=None)
N = int(df.values[0][0])

####
out = []
for i in xrange(1,N+1):
	numr = []
	occu = []
	s = list(str(df.values[i][0]))
	if len(s)==1:
#		print s
		r = int(s[0])
#		print r
		out.append([[r],[1]])
		continue
	numr.append(int(s[0]))
	occu.append(1)
	for j in xrange(1,len(s)):
		t = int(s[j])
		if t == numr[-1]:
			occu[-1]=1+occu[-1]
			if j == len(s)-1:
				out.append([numr,occu])
#				print out[-1]
				continue
		elif t > numr[-1]:
			numr.append(t)
			occu.append(1)
			if j == len(s)-1:
				out.append([numr,occu])
#				print out[-1]
				continue
		else:
			##numr[-1] reduces by one
			##everything else is 9
			##There might not be anything else.
			##Might merge [-1] into [-2]

			if numr[-1] == 1:
				##Then everything so far was a 1.
				## it is the length of s -1 and everything is a 9.
				numr = [9]
				occu = [len(s)-1]
				##add to out
				out.append([numr,occu])
#				print out[-1]
				break
			else:
				l = len(numr)
				if l == 1: ## And not 1
					##Reduce leading number by 1
					##And everything is a 9
					newnumr = [numr[0]-1, 9]
					newoccu = [1, len(s)-1]
					out.append([newnumr,newoccu])
#					print out[-1]
					break
				else:
					##Reduce last number by 1
					##Maybe merge into previous
					##And everything else is a 9
					newnumr = [numr[-1]-1, 9]
					newoccu = [1, len(s[j::])]
					if numr[-1]-1 == numr[-2]:
						occu[-2]=occu[-2]+1
						occu[-1]=occu[-1]+len(s[j::])-1
						numr[-1]=9
					else:
						numr[-1]=newnumr[0]
						occu[-1]=newoccu[0]
						numr.append(9)
						occu.append(newoccu[1])
					out.append([numr,occu])
#					print out[-1]
					##Write
					break
####

lines=[]
for i in range(len(out)):
	so = r'Case #' + str(i+1) + ': '
	case = out[i]
	numrs = case[0]
	occus = case[1]
	tog = zip(occus, numrs)
	for n, o in tog:
		for N in range(n):
			so = so + str(o)
	lines.append(so)





with open("mout.txt", "w") as text_file:
#	toPrint = ''
#	for i in range(len(out)):
#		toPrint = toPrint + r'Case #' + str(i+1) + ': '
#		for j in range(out[i][1][j]):
#			toPrint = toPrint + out[i][0][j]
	for line in lines:
		text_file.write(line + "\n")
