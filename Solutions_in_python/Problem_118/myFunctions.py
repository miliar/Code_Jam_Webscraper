import re
import math
import numpy as np
import string
from decimal import *

##########################################################################################################################

def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

##########################################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()

##########################################################################################################################

def StrToNumList(s):
	#return [int(x) for x in re.findall('[0-9\-]+',s)]
	return [int(x) for x in s[:-1].split()]

##########################################################################################################################

def StrToNum(s):
	return int(s[:-1])

##########################################################################################################################

def innerProd(x,y):
	return sum([i*j for i,j in zip(x,y)])

##########################################################################################################################

def storeCredit(L):
	credit, items = StrToNum(L[0]), StrToNumList(L[2])
	d = {}
	for item, price in enumerate(items,1):
		if price in d:
			return "%s %s" %(d[price], item)
		else:
			d[credit-price] = item

##########################################################################################################################

def reverseWords(s):
	return ' '.join(reversed(s.split()))

##########################################################################################################################

def minScalarProd(L):
	v1, v2 = StrToNumList(L[0]), StrToNumList(L[1])
	return innerProd(sorted(v1), reversed(sorted(v2)))

##########################################################################################################################

def validate_customer(flav, customer):
	nLikes, pref = customer[0], customer[1:]
	malted_flav_index = "IMPOSSIBLE"
	for i in range(nLikes):
		if pref[2*i+1] == flav[pref[2*i]-1]:
			return "Satisfied"
		elif pref[2*i+1] == 1 and flav[pref[2*i]-1]==0:
			malted_flav_index = pref[2*i]-1
	return malted_flav_index

##########################################################################################################################

def validate_preference(f, c):
	for cust in c:
		r = validate_customer(f, cust)
		if r == "Satisfied":
			pass
		elif r == "IMPOSSIBLE":
			return r
		else:
			f[r] = 1
			c.remove(cust)
			return validate_preference(f,c)
	return ' '.join([str(x) for x in  f])

##########################################################################################################################

def milkShake(L):
	flavours = [0]*StrToNum(L[0])
	customers = [StrToNumList(c) for c in L[2:] ]
	return validate_preference(flavours, customers)

##########################################################################################################################

def pad(lt, rt):
    if rt[:1] == lt[-1:]:
        lt += ' '
    return lt + rt

##########################################################################################################################

def t9(s):
	s = s[:-1]
	if not s:
		return ''
	keymap = " ,,abc,def,ghi,jkl,mno,pqrs,tuv,wxyz".split(',')
	t9map = {char:str(key)*repeat for key,label in enumerate(keymap) for repeat,char in enumerate(label,1)}
	return reduce(pad, map(t9map.get, s))

##########################################################################################################################

def recur_multi(m,n):
	if n == 1:
		#print m, 'n=1 so returned'
		return m
	else:
		if n % 2 == 0:
			#print m, n, 'n is even so disected into two of:', n/2
			return np.dot(recur_multi(m,n/2),recur_multi(m,n/2))%1000
		else:
			#print m, n, 'n is further result is:', (np.mat(m)*np.mat(recur_multi(m,n-1)))%1000
			return np.dot(m,recur_multi(m,n-1))

##########################################################################################################################

def matrix_mult(A, B):
	C = [[0, 0], [0, 0]]
	for i in range(2):
		for j in range(2):
			for k in range(2):
				C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
	return C

##########################################################################################################################

def fast_exponentiation(A, n):
	if n == 1:
		return A
	else:
		if n % 2 == 0:
			A1 = fast_exponentiation(A, n/2)
			return matrix_mult(A1, A1)
		else:
			return matrix_mult(A, fast_exponentiation(A, n - 1))

##########################################################################################################################

def numbers_power(s):
	n = StrToNum(s)
	#return (recur_multi(np.mat( [[3, 5], [1, 3]]),n)[0,0]*2 + 999)%1000
	A = [[3, 5], [1, 3]]
	A_n = fast_exponentiation(A, n)
	return (2 * A_n[0][0] + 999) % 1000

##########################################################################################################################

def alien_lang(s,d):
	test = reduce(lambda x, y: x.strip() + ' ' + y.strip(), [item for item in d])
	s = s.strip().replace(')',']')
	s = s.replace('(','[')
	return len(re.findall(s,test))

##########################################################################################################################

def googlerese(s):
	s = s.strip()
	d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	return reduce(lambda x, y: x + y, map(d.get, s))

##########################################################################################################################

def dance_scores(l):
	l = StrToNumList(l)
	n = l.pop(0)
	s = l.pop(0)
	p = l.pop(0)
	if p == 0:
		return len(l)
	elif p == 1:
		return len(filter(lambda x: x > 0, l))
	else:
		return len(filter(lambda x: x > 3*(p-1),l)) + min(s,len(filter(lambda x: x == (3*p-3) or x == (3*p-4), l)))

##########################################################################################################################

def permute(s,b):
	s = str(s)
	l = set([s[i:]+s[:i] for i in range(1,len(s)) if int(s) < int(s[i:]+s[:i]) <= b ])
	#ans = 0
	#if len(l) > 1:
		#ans = math.factorial(len(l))/(math.factorial(len(l)-2)*2)
		#ans = len(l)
	return len(l)

##########################################################################################################################

def rec_nums(l):
	a, b = StrToNumList(l)
	d = {}
	d = {str(i):i for i in range(a, b + 1)}
	ans = 0
	while d:
		item, l = permute(d.iterkeys().next(),a,b)
		[d.pop(key,None) for key in l]
		ans += item
	return ans

##########################################################################################################################

def rec_nums1(l):
	a, b = StrToNumList(l)
	ans = 0
	for i in range(a,b+1):
		item = permute(i,b)
		ans += item
	return ans

##########################################################################################################################

def mirrors(l):
	
	return ans

##########################################################################################################################

def StrToDecimalList(s):
	#return [int(x) for x in re.findall('[0-9\-]+',s)]
	getcontext().prec = 6
	return [Decimal(x) for x in s[:-1].split()]

##########################################################################################################################

def pass_prob(l):
	getcontext().prec = 6
	n, m = StrToNumList(l[0])
	p = StrToDecimalList(l[1])
	cp = p
	for i in range(1,n):
		cp[i] = cp[i]*cp[i-1]
	cp.reverse()
	res = []
	#res.append(cp[n-1]*(m-n+1) + (1-cp[n-1])*(2*m+2-n))
	res.append(m + 2)
	for i in range(0,n-1):
		res.append(cp[i]*(m-n+2*i+1) + (1-cp[i])*(2*m-n+2*i+2))
	return min(res)

##########################################################################################################################

def boxes(l):
	n, m = StrToNumList(l[0])
	box = StrToNumList(l[1])
	toy = StrToNumList(l[2])
	box_list = []
	toy_list = []
	for i in range(0,len(box),2):
		box_list = box_list + [box[i+1]]*box[i]
	for i in range(0,len(toy),2):
		toy_list = toy_list + [toy[i+1]]*toy[i]
	box_num = 1
	toy_num = 1
	alt = True
	packed = 0
	while (box_num<len(box)) and (toy_num<len(toy)):
		print 'box_num:', box_num, 'toy_num:', toy_num 
		if box[box_num] == toy[toy_num]:
			if box[box_num -1] >= toy[toy_num - 1]:
				packed += toy[toy_num - 1]
			else:
				packed += box[box_num - 1]
			toy_num += 2
			box_num += 2
			print 'entered 1 and packed is now:', packed
		elif (toy_num + 2<len(toy)) and alt:
			print 'entered 2'
			if box[box_num] == toy[toy_num + 2]:
				toy_num += 2
			alt = False
		elif (box_num + 2<len(box)) and not alt:
			print 'entered 3'
			if box[box_num + 2] == toy[toy_num]:
				box_num += 2
			alt = True
		else:
			print 'entered 4'
			toy_num += 2
			box_num += 2
	return packed

##########################################################################################################################

def diamond(g):
	graph = {'A': ['B', 'C','E'],
	             'B': ['A','C', 'D'],
	             'C': ['D'],
	             'D': ['C'],
	             'E': ['F','D'],
	             'F': ['C']}



class MyQUEUE: # just an implementation of a queue
	
	def __init__(self):
		self.holder = []
		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result


path_queue = MyQUEUE() # now we make a queue


def BFS(graph,start,end,q):
	temp_path = [start]
	q.enqueue(temp_path)
	valid_paths = 0
	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		#print tmp_path
		if last_node == end:
			#print "VALID_PATH : ",tmp_path
			valid_paths + 1
		for link_node in graph[last_node]:
			if link_node not in tmp_path:
				new_path = []
				new_path = tmp_path + [link_node]
				q.enqueue(new_path)

##########################################################################################################################

def tttt_sol(X,O,nil_flag):
	winner = ''
	for i in range(4):
		if sum(X[i]) == 4:
			winner = 'X won'
			return winner
		if sum(O[i]) == 4:
			winner = 'O won'
			return winner

	for j in range(4):
		if X[0][j] + X[1][j] + X[2][j] + X[3][j] == 4:
			winner = 'X won'
			return winner
		if O[0][j] + O[1][j] + O[2][j] + O[3][j] == 4:
			winner = 'O won'
			return winner

	if X[0][0] + X[1][1] + X[2][2] + X[3][3] == 4:
		winner = 'X won'
		return winner

	if X[0][3] + X[1][2] + X[2][1] + X[3][0] == 4:
		winner = 'X won'
		return winner

	if O[0][0] + O[1][1] + O[2][2] + O[3][3] == 4:
		winner = 'O won'
		return winner

	if O[0][3] + O[1][2] + O[2][1] + O[3][0] == 4:
		winner = 'O won'
		return winner

	if nil_flag == True:
		return 'Game has not completed'

	return 'Draw'

##########################################################################################################################

def tttt_matrix(input):
	X = []
	O = []
	nil_flag = False
	for i in range(4):
		Xs = []
		Os = []
		for j in range(4):
			if input[i][j] == 'T':
				Xs.append(1)
				Os.append(1)
			elif input[i][j] == 'X':
				Xs.append(1)
				Os.append(0)
			elif input[i][j] == 'O':
				Xs.append(0)
				Os.append(1)
			else:
				Xs.append(0)
				Os.append(0)
				nil_flag = True
		X.append(Xs)
		O.append(Os)
	return X, O, nil_flag

##########################################################################################################################

def lawn_matrix(cases):
	X = []
	nil_flag = False
	for i in range(4):
		Xs = []
		Os = []
		for j in range(4):
			if input[i][j] == 'T':
				Xs.append(1)
				Os.append(1)
			elif input[i][j] == 'X':
				Xs.append(1)
				Os.append(0)
			elif input[i][j] == 'O':
				Xs.append(0)
				Os.append(1)
			else:
				Xs.append(0)
				Os.append(0)
				nil_flag = True
		X.append(Xs)
		O.append(Os)
	return X, O, nil_flag

##########################################################################################################################

def lawn_solve(A,N,M):
	global_min = min([min(line) for line in A])
	row_flags = [0]*N
	col_flags = [0]*M
	for i in range(N):
		for j in range(M):
			if A[i][j] == global_min:
				if row_flags[i] == 1 or global_min*M == sum(A[i]):
					row_flags[i] = 1
					continue
				elif col_flags[j] == 1 or global_min*N == sum([A[k][j] for k in range(N)]):
					col_flags[j] = 1
					continue
				else:
					return "NO"
	return "YES"

# def lawn_solve(A,N,M):
# 	global_min = min([min(line) for line in A])
# 	row_flags = [0]*N
# 	col_flags = [0]*M
# 	for i in range(N):
# 		for j in range(M):
# 			if A[i][j] == global_min:
# 				if row_flags[i] == 1 or global_min*M == sum(A[i]):
# 					row_flags[i] = 1
# 					continue
# 				elif col_flags[j] == 1 or global_min*N == sum([A[k][j] for k in range(N)]):
# 					col_flags[j] = 1
# 					continue
# 				else:
# 					return "NO"
# 	return "YES"

##########################################################################################################################

def row_mins(input_row):
	m = min(input_row)
	row_mins = [i for i, j in enumerate(a) if j == m]
	return row_mins

##########################################################################################################################

def gen_palindromes():
	d1 = [1,2,3]
	d2 = [11,22,33]
	d3 = [(a+b*10+a*100) for a in (1,2,3) for b in range(10)]
	d4 = [(a+b*10+b*100+a*1000) for a in (1,2,3) for b in range(10)]
	d5 = [(a+b*10+c*100+b*1000+a*10000) for a in (1,2,3) for b in range(10) for c in range(10)]
	d6 = [(a+b*10+c*100+c*1000+b*10000+a*100000) for a in (1,2,3) for b in range(10) for c in range(10)]
	d7 = [(a+b*10+c*100+d*1000+c*10000+b*100000+a*1000000) for a in (1,2,3) for b in range(10) for c in range(10) for d in range(10)]
	palindromes = d1+d2+d3+d4+d5+d6+d7
	return palindromes

##########################################################################################################################

def check_palindrome(num):
	return str(num)[::-1]==str(num)

##########################################################################################################################

def palindrome_num(C,D,p):
	sublist = [x for x in p if x >= C and x <= D]
	sublist_sqr = map(lambda x: x*x, sublist)
	cnt = 0
	for i in sublist_sqr:
		if check_palindrome(i):
			cnt += 1
	return cnt

##########################################################################################################################

