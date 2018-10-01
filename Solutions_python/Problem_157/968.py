import math
import fileinput
f = fileinput.input()

table = []
table.append(["1","i","j","k"])
table.append(["i","-1","k","-j"])
table.append(["j","-k","-1","i"])
table.append(["k","j","-i","-1"])

def multiply(a,b):
	neg = 1
	chara = 0
	charb = 0
	indexa = 0
	indexb = 0
	if a[chara] == '-':
		neg *= -1
		chara = 1

	if b[charb] == '-':
		neg *= -1
		charb = 1

	if a[chara] == 'i':
		indexa = 1
	elif a[chara] == 'j':
		indexa = 2
	elif a[chara] == 'k':	
		indexa = 3

	if b[charb] == 'i':
		indexb = 1
	elif b[charb] == 'j':
		indexb = 2
	elif b[charb] == 'k':
		indexb = 3

	c = table[indexa][indexb]
	charc = 0
	if c[charc] == '-':
		neg *= -1
		charc = 1

	if neg == -1:
		return '-'+c[charc]
	
	return c[charc]
		
def sol(l,str,x):
	n = l * x
	iarr = [None]*n
	karr = [None]* n
	ch = '1'
	for i in xrange(x):
		for j in xrange(l):
			ch = multiply(ch,str[j])
			index = i * l + j
			if ch == 'i':
				iarr[index] = index
			elif index == 0:
				iarr[index] = -1
			else:
				iarr[index] = iarr[index -1]	
			
		
	
	if iarr[n-1] == -1:
		return "NO"

	ch = '1'
	for i in xrange(x-1,-1,-1):
		for j in xrange(l-1,-1,-1):
			ch = multiply(str[j],ch)
			index = i * l + j
			if ch == 'k':
				karr[index] = index
			elif index == n-1:
				karr[index] = -1
			else:
				karr[index] = karr[index+1]
			
			
		
	if karr[0] == -1:
		return "NO"
	
	jarr_rev = []
	ch = '1'
	for i in xrange(l):
		ch = multiply(ch,str[i])
		jarr_rev.append(ch)	
		
	jarr = []
	ch = '1'
	for i in xrange(l-1,-1,-1):
		ch = multiply(str[i],ch)
		jarr.append(ch)

	prod = product(str,l)
	for a in xrange(n):
		if a == iarr[a]:
			res = isj(a+1,karr[a]-1,str,x,l,prod,jarr,jarr_rev)
			if res:
				return "YES"
			
		
	
	return "NO"

def product(str,l):
	ch = '1'
	for i in xrange(l):
		ch = multiply(ch,str[i])
	
	return ch 

def isj(start, end , str,x,l, prod, jarr, jarr_rev):
	if start > end:
		return False

	a = start / l
	b = end / l
	i = start % l
	ch = '1'
	if b == a:
		for tt in xrange(end-start+1):
			ch = multiply(ch,str[i])
			i += 1
		
	else :
		ch = jarr[l - i - 1]

	neg = -1
	if b - a > 1:  
		rem = (b - a - 1)%4
		if rem == 0:
			ch = multiply(ch,prod)
		elif rem == 1:
			ch = multiply(ch,"-1")
		elif rem == 2:
			negprod = multiply(prod,"-1")
			ch = multiply(ch,negprod)
		
	
	if b > a:
		left = end % l
		ch = multiply(ch,jarr_rev[left])
		
	if ch== 'j':
		return True
	
	return False

def read_input():
	t = int(f.readline())
	input_str = []
	input_x =  []
	input_l = []
	for i in xrange(t):
		line1arr = f.readline().split()
		input_x.append(int(line1arr[1]))
		input_l.append(int(line1arr[0]))
		input_str.append(f.readline())

	case = 1
	for input in input_str:
		res = sol(input_l[case-1],input,input_x[case-1])
		output = "Case #"+str(case)+": "+res
		print output
		case += 1
	

read_input()
#print sol(3,'ijk',1)
#print sol(
#print isj(1,1,"ijk",1,3)
