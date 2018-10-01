from math import *;
INPUT_NAME = 'C-small-attempt0.in'
OUTPUT_NAME = 'C-small.out'
#INPUT_NAME = 'C.in'
#OUTPUT_NAME = 'C.out'

nck = [[0 for i in xrange(110)] for j in xrange(110)];

def make_nck():
	for i in xrange(110):
		nck[i][0] = 1
	for i in xrange(1,110):
		for j in xrange(1,110):
			nck[i][j] = nck[i-1][j] + nck[i-1][j-1]

def sqrt_integer(n):    
    (d, r) = divmod(int(n).bit_length(), 2)
    x = 2**(d+r)
    while(True):
        y = (x + n//x)//2
        if(y >= x):
            return x
        x = y

def count_strings(a, b, n):
	if a+b > n:
		return 0
	return nck[n-1][a+b-1]*nck[a+b][a]; # #strings NOT beginning with zero and with a 1s, b 2s and n-a-b 0s

def count_with_zeros(a,b,n):
	if a+b > n:
		return 0
	return nck[n][a+b]*nck[a+b][a]
	
def allGenerators(L, m, zeros=False):
	# all generators length L with midpt_sqr = m
	if m >=9:
		return 0
	total = 0
	max1s = min((9-m)//2, L)
	for num1s in xrange(max1s+1):
		max2s = min((9-m-2*num1s)//8,L-num1s)		
		for num2s in xrange(max2s+1):			
			if(zeros):
				total += count_with_zeros(num1s, num2s, L)
			else:
				total += count_strings(num1s, num2s, L)	
	return total	
	
def numSPal(k,sub=0,zeros=False):
	#number of square-able palindromes of length k
	if(k<=0):
		return 0 	
	if(sub > 9):
		return 0
	if(k==1):		
		if(sub==0):		
			return 3 # 1,2,3
		elif(4+sub<10):
			return 3 if zeros else 2
		elif(1+sub<10):
			return 2 if zeros else 1
		else:
			return 1 if zeros else 0
		
	(LG,rem) = divmod(k,2)
	if(rem==0): 	#even
		return allGenerators(LG,sub,zeros)
	else:			#odd
		total = 0
		for mid in xrange(3):
			total += allGenerators(LG,mid**2+sub,zeros)
		return total
		
def sqrp_below(n):
	# Find # of 'squarable' palindromes less than or equal to n
	L = [int(i) for i in str(n)]
	numdigits = len(L)
	if(numdigits == 1):
		if(n<3):
			return n
		else:
			return 3
		
	total = 0
	for nd in xrange(numdigits):				
		total += numSPal(nd)		
	
	# the hard part is for number of digits EQUAL to the number in question
	(LG,rem) = divmod(numdigits,2)
	splitter = 0 # position at which the palindrome first differs from the string
	sofar = 0
	split_out = False			
	while(splitter<LG):				
		if(L[splitter]>=3): # force split here			
			total += numSPal(2*(LG-splitter)+rem,sofar)  # all palindromes starting AT splitter with 1 or 2, NOT starting with zero
			if(splitter>0):
				if rem == 0 and splitter == LG-1 and sofar < 10:
					total += 1
				else:
					total += numSPal(2*(LG-splitter-1)+rem,sofar,True)	# palindromes with zero AT splitter, starting at next step (and possibly zero there too)				
					
			split_out = True
			break
		elif(L[splitter]==2): #try out 0,1
			if rem == 0 and splitter == LG-1 and sofar+2 < 10:
				total += 1
			else:
				total += numSPal(2*(LG-splitter-1)+rem,sofar+2*1,True) # palindromes with 1 AT splitter, starting at next step
			if(splitter>0):
				if rem == 0 and splitter == LG-1 and sofar < 10:
					total += 1
				else:
					total += numSPal(2*(LG-splitter-1)+rem,sofar,True) # palindromes with 0 AT splitter, starting at next step			
		elif(L[splitter]==1 and splitter>0): #try out 0
			if rem == 0 and splitter == LG-1 and sofar < 10:
				total += 1
			else:
				total += numSPal(2*(LG-splitter-1)+rem,sofar,True)
		#increment splitter and sofar for remaining palindromes, which follow the number up to splitter		
		sofar += 2*L[splitter]**2
		splitter+=1		
		if(sofar>9):
			split_out = True
			break
		
	if(not(split_out)):		
		# decide on the fine-print
		(x,y) = (L[:LG], L[-LG:])
		x.reverse()
		okay = True
		for i in xrange(len(x)):
			if(x[i]<y[i]):
				break
			if(x[i]>y[i]):
				okay = False
				break
		
		if(rem==1):
			total += max(L[LG],0) # add all middles beneath the current middle
		
		if(okay):
			total += 1	# add current middle if it will be small enough [also add "reflected first half" for even numbers]
					
	return total # with a lot of luck, this is the answer!
		
		
def solve(I):
	(sA,sB) = map(sqrt_integer, I)	
	if(sA**2 < I[0]):
		sA += 1
	# now sA**2 is smallest square >= A and sB**2 is largest square <= B
	# so we want the number of squarable palindromes with sA <= P <= sB
	return sqrp_below(sB) - sqrp_below(sA-1)
	
def fullsol(slst):
	make_nck()
	T = int(slst[0]) # number of test cases
	return [solve(map(int, i.split())) for i in slst[1:]]		
	
def makestring(row):
	# make a list into a string separated by spaces
	return ''.join([' '+str(i) for i in row])[1:]

def olwrite(fname, answers):
	# write outputs to file line by line [one-line outputs]
	f = open(fname, 'w')
	lines = ['Case #'+str(i+1)+': '+str(answers[i])+'\n' for i in xrange(len(answers))]
	f.writelines(lines)
	f.close()
	return
	
def sread(fname):
	f = open(fname, 'r')
	res = [x.strip() for x in f.readlines()]
	f.close()
	return res
	
stuff = sread(INPUT_NAME)
answers = fullsol(stuff)
olwrite(OUTPUT_NAME, answers)



	