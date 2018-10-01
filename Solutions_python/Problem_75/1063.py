import math
from decimal import Decimal


infile = open("B-large.in","r")
#infile = open("input.txt","r")
#infile = open("B-small-attempt2.in","r")
firstr = 0
case = 1
records = infile.readlines()
infile.close()

combine = {}
opposed = {}

i = 0
while i < len(records):
	#print records[i]
	if i == 0:
		i = i + 1
		continue
	rec = records[i].split(" ")
	n_com = int(rec[0])  # number of combined pairs
	next = 1
	if n_com != 0:
		for k in range(0,n_com):
			combelem = rec[k+next]
			key = combelem[0]+combelem[1]  # pair is the key
			combine[key] = combelem[2]
			key = combelem[1]+combelem[0]  # pair is the key
			combine[key] = combelem[2]
		next = next + n_com
		
	n_opp = int(rec[next])
	next = next + 1
	if n_opp != 0:
		for k in range(0,n_opp):
			oppelem = rec[k + next]
			key = oppelem[0] + oppelem[1]
			opposed[key] = 1
			key = oppelem[1] + oppelem[0]
			opposed[key] = 1
		next = next + n_opp
	
	n = int(rec[next])  # size of the list
	next = next + 1
	invoke = rec[next]
	final = []
	next = 0  # clear up
	# invocation
	for j in range(0,n):
		final.append(invoke[j])
		if len(final) > 1 :
			comb = final[len(final)-2]+final[len(final)-1]
			if comb in combine:
				final = final[:-2]
				final.append(combine[comb])
			else:
				for e in final[:-1] :
					opp = e + invoke[j]
					if opp in opposed:
						final = []
						break

	strf = ""
	for e in final:
		strf = strf + e + ", "
	strf = strf[:-2]
	print "Case #"+ str(case)+": ["+strf+"]"
	
	final = []
	combine = {}
	opposed = {}
	case = case + 1
	i = i + 1
	
		
