import pdb
import math

file = open('C-small-attempt1.in', 'r')
n = int(file.readline())

def mulp(a, b):
	if a == '1' and b == '1':
		return '1',0
	elif a == '1' and b == 'i':
		return 'i',0
	elif a == '1' and b == 'j':
		return 'j',0
	elif a == '1' and b == 'k':
		return 'k',0
	elif a == 'i' and b == '1':
		return 'i',0
	elif a == 'i' and b == 'i':
		return '1',1
	elif a == 'i' and b == 'j':
		return 'k',0
	elif a == 'i' and b == 'k':
		return 'j',1
	elif a == 'j' and b == '1':
		return 'j',0
	elif a == 'j' and b == 'i':
		return 'k',1
	elif a == 'j' and b == 'j':
		return '1',1
	elif a == 'j' and b == 'k':
		return 'i',0
	elif a == 'k' and b == '1':
		return 'k',0
	elif a == 'k' and b == 'i':
		return 'j',0
	elif a == 'k' and b == 'j':
		return 'i',1
	elif a == 'k' and b == 'k':
		return '1',1
	else:
		return '0',0

def D_mul(D):
	j = len(D) - 1
	count = 0
	while j > 0:
		a, b = mulp(D[j-1],D[j])
		D = D[:-2]
		D.append(a)
		count = count + b
		j = j - 1
	return D[0],count

for i in range(n):
	P = file.readline().strip().split(' ')
	P = [int(j) for j in P]
	L = P[0]
	X = P[1]
	D = file.readline().strip()
	#pdb.set_trace()
	if X % 4 == 0:
		res = 'NO'
	else:
		D = D * (X%12)
    	D = [j for j in D]
    	if L*X < 3:
        	res = 'NO'
    	else:
        	j = 1
        	count1 = 0
        	if D[0] != 'i':
				while len(D) > 1:
					r1, temp = mulp(D[j-1],D[j])
					D[j] = r1
					D = D[j:]
					count1 = count1 + temp
					if r1 == 'i':
						break
        	k = 1
        	count2 = 0
        	if D[-1] != 'k':
        		while len(D) > 1:
        			r2, temp = mulp(D[-(k+1)],D[-k])
        			D = D[:-k]
        			D[-1] = r2
        			count2 = count2 + temp
        			if r2 == 'k':
        				break
                    
        	if len(D) <= 2:
        		res = 'NO'
        	else:
        		r3, count3 = D_mul(D[1:-1])
        		if r3 == 'j' and (count1+count2+count3) % 2 == 0:
        			res = 'YES'
        		else:
        			res = 'NO'
	#pdb.set_trace()
	print "Case #%s: %s" % (str(i+1), res)
    
