from math import log2

# Input data
infile = input("Enter input filename: ") + ".in"
if infile == ".in": infile = "default.in"
with open(infile, 'r') as f:
	data = f.read().split("\n")
while data[-1].isspace() or not(data[-1]):
	data.pop()
	
testCases = int(data[0]) #number of cases
dataL = data.__len__() #length of data
results = []

#Functions
def gcd (x, y):
	"Calculates the Greatest Common Divisor with Euclidean algorithm"
	#gcd(x, y) = gcd(y, rem(x,y))
	remainder = 1;
	while remainder != 0:
		remainder = x % y
		x = y
		y = remainder
	return x
	
# Problem solve
case = 1
while case <= testCases:
	pq = data[case].split("/")
	case += 1
	p = int(pq[0])
	q = int(pq[1])
	gcdPQ = gcd(p,q)
	p /= gcdPQ
	q /= gcdPQ
	totalgen = round(log2(q))
	if 2**totalgen != q:
		results.append("impossible")
	else:
		results.append(totalgen-int(log2(p)))


# Output data
outfile = "out.txt"
with open(outfile, 'w') as f:
	for i in range(testCases):
		f.write("Case #%i: %s\n" % (i+1, str(results[i])))
			
