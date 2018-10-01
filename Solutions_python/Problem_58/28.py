import sys

class memoize:
  def __init__(self, function):
	self.function = function
	self.memoized = {}

  def __call__(self, *args):
	x = max(args[0],args[1])
	y = min(args[0],args[1])
	if x == y:
		return False
	if y == 1 or x%y==0:
		return True
	try:
		return self.memoized[args]
	except KeyError:
		self.memoized[args] = self.function(*args)
		return self.memoized[args]

def readListOfChars( inputFile ):
	return inputFile.readline().strip().split(" ")

def readListOfInts( inputFile ):
	return map( int, inputFile.readline().strip().split(" ") )

@memoize
def winner( a, b ):
	if a==b:
		return False

	x = max(a,b)
	y = min(a,b)
	
	if y==1 or x%y==0:
		return True
	
	maxK = x//y
	
	if not winner(y, x-(y*maxK)):
		return True
	if maxK > 1 and not winner(y,x-(y*(maxK-1))):
			return True
		
	return False

if( len(sys.argv) > 1 ):
	input = file( sys.argv[1] )
else:
	input = file("A-tiny.in")

NumCases = int(input.readline())

for case in range(NumCases):
	
	(A1, A2, B1, B2) = readListOfInts( input )

	winners = 0
	for A in range(A1,A2+1):
		for B in range(B1,B2+1):
			if winner( A, B ):
				winners += 1

	output = "Case #%d: %d" % ( case+1, winners )
	print output
	
