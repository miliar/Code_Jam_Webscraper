#
#
# PYTHON 3.2
#
# ./a.out < input.in  | grep -v '^#'
# ----------------------------------------------------------------------------
from fractions import gcd


# ----------------------------------------------------------------------------
# GLOBALS
#
comb = {}
opps = {}


# ----------------------------------------------------------------------------
# FOO
#
def hello():
	print("x")

# ----------------------------------------------------------------------------
# FOO
#
def test(x, oth):
	#print("### test {0}".format(x))
	for y in oth:
		if x > y:
			m = x % y
		else:
			m = y % x
			
		#print("### {0},{1},{2}".format(m,x,y))
		if m != 0:
			return False
	
	return True

# ----------------------------------------------------------------------------
# FOO
#
def iai(N, L, H, oth):
	
	for x in range(L,H+1):
		harm = test(x, oth)
		if harm:
			return str(x)
			
	return "NO"
			
		

# ############################################################################
# ############################################################################
# ############################################################################
# ############################################################################
if __name__ == "__main__":
	T = 1
	sss = ""
	
	#print("### Hello World!")
	sss = input()
	T = int(sss)
	#print("### {0} Cases".format(T))
	
	for i in range(0,T):
		# - Initialize Case Vars
		# - Read Case Input
		N, L, H =  [int(x) for x in input().strip().split()]
		Others = [int (x) for x in input().strip().split()]

		#print("### {0},{1},{2}".format(N, L, H))
		#print(Others)

		# !!!
		sol = iai(N, L, H, Others)
				
		
		print("Case #{0}: ".format(i+1) + sol)


