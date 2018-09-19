import re
import numpy as np
import string
import math
from decimal import Decimal
from operator import mul

##########################################################################################################################

def parseInputData_gen(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	first = finput.readline()
	rest = finput.readlines()	
	finput.close()
	return first, rest

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
	return innerProd(sorted(StrToNumList(L[0])), reversed(sorted(StrToNumList(L[1]))))

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

def t9_dict():
	keymap = " ,,abc,def,ghi,jkl,mno,pqrs,tuv,wxyz".split(',')
	#t9map = {char:str(key)*repeat for key,label in enumerate(keymap) for repeat,char in enumerate(label,1)}
	t9map = {}
	for key,label in enumerate(keymap):
		for repeat,char in enumerate(label,1):
			t9map[char] = str(key)*repeat
	return t9map

##########################################################################################################################

def t9(s,t9map):
	s = s[:-1]
	if not s:
		return ''
	return reduce(pad, map(t9map.get, s))

##########################################################################################################################

def last_3_Digits(n):
	return ('000'+str(n))[-3:]

##########################################################################################################################

def matrixMultiply(x,y):
	return np.dot(x,y)%1000

##########################################################################################################################

def matrixPow(x,n):
	if n==1:
		return x
	elif n%2==0:
		return matrixPow(matrixMultiply(x,x),n/2)
	else:
		return matrixMultiply(matrixPow(matrixMultiply(x,x),n/2),x)

##########################################################################################################################

def numbers(x,s):
	n = StrToNum(s)
	m = matrixPow(x,n)
	result = (2*m[0][0] - 1) % 1000
	return last_3_Digits(result)

##########################################################################################################################

def alien_language(s,words):
	searchStr = s[:-1].replace("(","[").replace(")","]")
	searchIt = re.compile(searchStr).search
	return len(filter(searchIt, words))

##########################################################################################################################

def tongues(line, myDict):
	return ''.join(map(myDict.get, line[:-1]))
	
##########################################################################################################################

def genPerm(n,b):
	s = str(n)
	return len(set([ s[i:]+s[:i] for i in range(1,len(s)) if n < int(s[i:]+s[:i]) <= b ]))

##########################################################################################################################

def recNum(s):
	a,b = StrToNumList(s)
	return sum([genPerm(i,b) for i in xrange(a,b+1)])

##########################################################################################################################

def danceScores(s):
	l = StrToNumList(s)
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

def getUnique(images,D):
	count = 0
	result = []
	while images:
		a,b = images.pop(0)
		if a**2 + b**2 <= D**2:
			result.append(str(a)+' '+str(b)+'\n')
			count += 1
			images = filter(lambda (x,y): a*x<0 or b*y<0 or (a!=0 and y -(b/a)*(x-a) - b != 0), images)
	writeOutput(result, 'MY', 'GRAPH', 'DATA')
	return count


def reflections(x1, x2, x0, y0, D, flag):
	images = []
	distance = 0
	while True:
		image = 2*x2 - x0
		distance += abs(image - x0)
		if distance <= D:
			if flag=='x':
				images.append((image,y0))
			else:
				images.append((y0,image))
		else:
			break
		x0, x1, x2 = image, x2, 2*x2 - x1
	return images


def findReference(hall):
	for key, label in enumerate(hall):
		if 'X' in label:
			return (label.find('X')+0.5, -(key+0.5))


def mirrors(L):
	H, W, D = StrToNumList(L[0])
	hall = [L[i+1][:-1] for i in range(H)]
	x0, y0 = findReference(hall)
	x1, x2, y1, y2 = 1-x0, W-1-x0, -1-y0, -H+1-y0
	x0, y0 = 0, 0
	images = reflections(x2, x1, x0, y0, D, 'x')  + reflections(x1, x2, x0, y0, D, 'x' )
	y_reflections = []
	for (x,y) in images:
		y_reflections +=  reflections(y2, y1, y, x, D, 'y') + reflections(y1, y2, y, x, D, 'y')
	images += y_reflections + reflections(y2, y1, y0, x0, D, 'y') + reflections(y1, y2, y0, x0, D, 'y')
	return getUnique(images,D)

##########################################################################################################################

def str_to_float_list(s):
	return [Decimal(x) for x in s[:-1].split()]

def password(l):
	m, n = StrToNumList(l[0])
	p = str_to_float_list(l[1])
	k = n + m + 1
	c = n + 1
	r = min(c + 1, k)
	pm = 1
	for i in p:
		pm *= i
		k -= 2
		r = min(r, k + c*(1 - pm))
	return str(r + Decimal('0.000000'))[:8] 

##########################################################################################################################

def kingdom_rush(n, l):
	stars = games = i = 0
	l = [StrToNumList(level)+[2] for level in l]
	l.sort(key = lambda tup: tup[1])
	while stars < n*2:
		if l[i][1] <= stars:
			stars, games, l[i][2], i = stars+l[i][2], games+1, 0, i+1
		else:
			for j in range(n-1, -1, -1):
				if l[j][0] <= stars and l[j][2] == 2:
					stars, games, l[j][2] = stars+1, games+1, l[j][2]-1
					break
			else:
				return "Too Bad"
	return games

##########################################################################################################################

def find_inheritance(i, l):
	dest = []
	for j in range(1, len(l[i])):
		newi = l[i][j]-1
		while True:
			if len(l[newi]) > 1:
				pass
			else:
				break
			newi = l[newi][1] - 1
		dest.append(newi)
	for node in dest:
		if dest.count(node) > 1:
			return "Yes"
	else:
		return "No"
		

def diamond(n, l):
	l = [StrToNumList(item) for item in l]
	for i in range(len(l)):
		if len(l[i]) > 2:
			return find_inheritance(i, l)
	else:
		return "No"


##########################################################################################################################


def magic_trick(l):
	row1 = l[l[0][0]]
	row2 = l[l[5][0] + 5]
	common = list(set(row1) & set(row2))
	num_len = len(common)
	if num_len == 1:
		return common[0]
	elif num_len > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"
	










