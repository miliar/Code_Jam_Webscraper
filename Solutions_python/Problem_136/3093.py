#@author Slolean
#A cookie Problem
import math
def input_case():
	T = input()#number of test cases
	info =[]
	for i in range(T):
		cfx= []
		val = raw_input()
		cfx.append(i+1)#[testcase,C,F,X]
		for itm in val.split():
			cfx.append(itm)
		info.append(cfx)
	return info

def aux_fun(C,n,F):
	i = 1
	val0 = 0
	while(i<=n):
		val0+=C/(2.0+(i-1)*F)
		i+=1
	return val0
	
def aux_fun_second(X,n,F):
	i = 0
	val1 = X/2.0
	while(i<=n):
		val1=X/(2.0+i*F)	
		i+=1
	return val1
	
	
#fucntion to be minimised
def time_fun(N,C,F,X):
	#number of farms,Cost,new rate, Target cookie, default rate
	#for n<0 not consistant with the solution
	return aux_fun(C,N,F)+aux_fun_second(X,N,F)
	

#def minimize(n_min,n_max,C,F,X):
#	min_idx = min(n,key=time_fun)
#	min_val = time_fun(min_idx)
	
def cookie_problm(inf):
	#inf[0]=case,inf[1]=C,inf[2]=F,inf[3]=X
	#intializations
	X = float(inf[3])
	F = float(inf[2])
	C = float(inf[1])
	r = 2 #cookie rate
	n = (F*X-r*C)/(F*C)
	if n<0:
		n=0
	n_floor=math.floor(n)
	n_ceil=math.ceil(n)
	v1=time_fun(n_floor,C,F,X)
	v2=time_fun(n_ceil,C,F,X)
	val = min(v1,v2)
	return val 
		
		
	
def main():
	a = input_case()
	#print a
	for i in a:
		t = cookie_problm(i)
		print 'Case #%i: %s'%(i[0],t)
	
	
if __name__=='__main__':
	main()
