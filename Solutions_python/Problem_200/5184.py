""" Tidy numbers """
import sys 

def from_key_board():
	L  = []
	for i in range(T):
		L.append([])
		N = input("")
		if not (N>=1 and N<=1000):
			break 
		for v in range(1, N+1):
			k = str(v)
			L[i].append(v)
			for j in range(1, len(k)):
				if not (k[j] >= k[j-1]):
					L[i].pop()
					break

	for i in range(len(L)):
		if len(L[i]):
			w = "Case #"+str(i+1)+": "
			print w + str(L[i][-1])
		
def tmp(N)	:
	global LL
	if (N>=1 and N<=1000):
		for v in range(1, N+1):
			k = str(v)
			LL[i].append(v)
			for j in range(1, len(k)):
				if not (k[j] >= k[j-1]):
					LL[i].pop()
					break
	

			
			
			
		
		
if len(sys.argv) == 2:
	f = open(sys.argv[1], 'r')
	L = f.readlines()[1:]
	LL = []
	for i in range(len(L)) :
		LL.append([])
		int_repr = int(L[i])
		tmp(int_repr)
	f.close()
	
	
	f = open("tmp.txt", "w")
	for i in range(len(LL)):
		if len(LL[i]):
			w = "Case #"+str(i+1)+": "
			print w + str(LL[i][-1])
			f.write((w + str(LL[i][-1]))+"\n")
	f.close()
			
	
else :
	try :
		T = input("")
		if not (T>=1 and T <= 100 ):
			import sys 
			print "Error"
			sys.exit()
		from_key_board()
			
	except IOError, e:
		print e
	



	
	
	
	
		 
"""		

f = open("B-small-attempt0.in", "r")
s = 0
for l in f :
	val = int(l)
	L.append([])
	if not (val >=1 and val <=1000):
		break 
	for i in range(1, val + 1):
		k = str(i)
		L[s].append(i)
		for j in range(1, len(k)):
			if not (k[j] >= k[j-1]):
					L[i].pop()
					break
		s += 1
print L
		
"""
"""		
f = open("B-small-attempt0.in", "r")
s = 0
for line in f:
	int_repr = int(line)
	L.append([])
	for i in range(1, int_repr + 1):
		L.append(line[i])
		for j in range(1, len(str(i))):
			if not (i[j] >= i[j-1]):
				L[s].pop()
				s -= 1
				break 
			s+= 1
print L
				
		
		
				
				
				
				
				
			


f.close()
"""
