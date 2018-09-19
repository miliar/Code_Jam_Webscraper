import time
import sys
import string
starttime,sol = time.time(), 0

def googleDancers(n, result = 0):
	temp = n.split(" ")
	n = int(temp[0])
	s = int(temp[1])
	p = temp[2]
	t = temp[3::]
	for x in t:
		#print "for t =", x,
		if p == '0' :
			result += 1
			#print "very low standards so everyone passes"
			continue
		if p == '1' :
			if int(x) > 0:
				result += 1
			#	print "low standards so everyone passes"
				continue
			else :
				continue
		compare_a = float(x)
		compare_r = (float(p) - 1.0)*3.0
		if compare_a > compare_r :
			#print "normail increase"
			result += 1
			continue 
		if s > 0 :
			if compare_a == compare_r or compare_a == compare_r - 1:
			#	print compare_a, compare_r, "surprise used"
				result += 1
				s -= 1
				continue
		continue
	return result



file_1 = open('B-large.in','r')
file_2 = open('GJ_2_sol_L.txt', 'w')
numoflines = int(file_1.readline())

for x in range(numoflines):
	print >> file_2, "Case #{0}: {1}".format(x+1, str(googleDancers(file_1.readline().strip())).strip())



print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	