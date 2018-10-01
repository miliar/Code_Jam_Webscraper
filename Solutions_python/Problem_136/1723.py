#Gonzalo Ciruelos
#Problem B
import sys
sys.setrecursionlimit(10000)

'''
Some calculations:
I wanna know, supposing I bought the farm, I will catch up to what would 
have happened if I didn't bought, so it is like a cinematics problem in
physics:

c/s means cookies per second
t   means time, it is a variable

COST+ 2c/s * t = 0 + (2+F)c/s * t
t = COST/F

So I will catch up in COST/FARM_YIELD seconds

The cookies I will have in that moment are (2+F)*COST/F and that is
greater than COST



In that moment, I can buy or not buy, so it is the same than before


COST * ((2+F)/F - 1) + (2+F) * t = (2+F+F) * t
t = COST((2+F)/F - 1)/F

At that moment, I'll have 
((2+F)/F-1)*COST/F cookies

And so on....


'''

def what_to_do(C, F, X, velocity = 2.0, seconds_accum = 0):
	
	time_required = C/F
	
	if C+velocity*(time_required) > X: #easiest case
		return seconds_accum + X/velocity
	else: #I have to buy in the first round
		seconds_accum += C/velocity
		velocity = velocity + F
		
		if X == 0:
			return seconds_accum
		else:
			return what_to_do(C, F, X, velocity, seconds_accum)
	

f = open('B-small-attempt0.in', 'r')
case_no = 1
for game in range(int(f.readline())):

	arg = map(float, f.readline()[:-1].split(' '))
	result = what_to_do(arg[0], arg[1], arg[2])
	
	print 'Case #'+str(case_no)+': '+str(round(result, 7))
	
	case_no+=1
