import math

def check_f_n_s(A,B):
	count=0
	for i in range(A,B+1):
		sq_rt=math.sqrt(i)
		if str(i)==str(i)[::-1]:
			if sq_rt==int(sq_rt):
				if str(int(sq_rt))==str(int(sq_rt))[::-1]:
					count+=1
	return count

#INPUT
for i in range(input()):
	A,B=[int(x) for x in raw_input().split(' ')]
	C=check_f_n_s(A,B)
	print "Case #"+str(i+1)+": "+str(C)