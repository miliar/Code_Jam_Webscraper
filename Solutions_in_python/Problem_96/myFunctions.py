import re
import numpy as np
import string
import math

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

