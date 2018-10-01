from numpy import array,zeros,where,nonzero,count_nonzero
 
		
def mawn(lawn):
	yes="YES"
	no="NO"
	dim = lawn.shape
	row = dim[0]
	col = dim[1]
	
	curLawn = lawn
	curmin = curLawn.min()
	x,y = where (curLawn==curmin)
	numOfMin = x.shape[0]

	
	while numOfMin!=(row*col):
	
		marked = zeros (numOfMin)
		for point in xrange (numOfMin):
			if marked[point]==0:
				r=x[point]
				c=y[point]
				por= (nonzero (x==r))[0]
				poc= (nonzero (y==c))[0]
				if len(por)==col:
					marked[por] =1
				elif len(poc)==row:
					marked[poc]=1
				else:
					return no
					
		n= curLawn[curLawn>curmin]
		curmin =n.min() #new min
		for mins in xrange (numOfMin):
			curLawn[x[mins],y[mins]] = curmin
		#print curLawn
		x,y = where (curLawn==curmin)
		numOfMin = x.shape[0]
			
	return yes

	
	
if __name__ == '__main__':

	f = open('B-large.in', 'r')
	num_samples = int(f.readline())

	for i in range(num_samples):
		dim = f.readline().split()
		row = int(dim[0])
		col = int(dim[1])
		lawn = zeros ((row, col))
		for k in xrange (row):
			line = f.readline().split()
			for j in xrange (col):
				lawn [k,j] = line [j]
		#print lawn
		print "Case #" + str(i+1) + ": "+  mawn(lawn)
