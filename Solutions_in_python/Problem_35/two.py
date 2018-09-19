import sys
def main():
	filename=sys.argv[1]
	f=open(filename,'r')
	outf=open('output.txt','w')
	tcCount = int(f.readline())
	for n in range(tcCount):
		outline = 'Case #'+str(n+1)+': '
		outf.write(outline+'\n');
		#print outline
		line = str.split(f.readline())
		m = int(line[0])
		n = int(line[1])
		matrix = []
		linkmatrix = []
		finalmatrix = []
		for j in range(m):
			row = str.split(f.readline())
			matrix.append(map(int, row))
			linkmatrix.append([])
			finalmatrix.append([])
			for k in range(n):
				linkmatrix[j].append([])
				finalmatrix[j].append('1')
		#printmat(matrix,m,n)
		#print linkmatrix		
		#Mark the sinks and the links
		sinklist = []
		
		for i in range(n):
			for j in range(m):
				
				flow = checkFlow(matrix, j, i, m, n)
				if flow[0] == j and flow[1] == i:
					sinklist.append((j,i))
				else:
					#print i,j,"flows to",flow
					linkmatrix[flow[0]][flow[1]].append((j,i))
		#printmat(linkmatrix,m,n)
		charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		numlist = range(1,27)
		charpos = 0
		for tup in sinklist:
			#start building stack
			label = numlist[charpos]
			charpos = charpos+1
			stack = []
			stack.append(tup)
			while len(stack) > 0:
				curr = stack.pop(0)
				finalmatrix[curr[0]][curr[1]] = label
				links =  linkmatrix[curr[0]][curr[1]]
				stack.extend(links)
				
		
		labels = {}
		charpos = 0
		for i in range(m):
			for j in range(n):
				value = finalmatrix[i][j]
				if labels.has_key(value):
					finalmatrix[i][j] = labels[value]
				else:
					labels[value]=charlist[charpos]
					charpos = charpos+1
					finalmatrix[i][j] = labels[value]

		#printmat(finalmatrix,m,n)
					
		for i in range(m):
			for j in range(n):
				outf.write(finalmatrix[i][j])
				outf.write(" ")
			outf.write("\n")

	f.close()
	outf.close()
	
def checkFlow(arr , i , j, m, n):
	min = arr[i][j]
	r = i
	c = j
	if isValid(i-1,j,m,n) and arr[i-1][j] < min:
		min = arr[i-1][j]
		r = i-1
		c = j
	if isValid(i,j-1,m,n) and arr[i][j-1] < min:
		min = arr[i][j-1]
		r = i
		c = j-1
	if isValid(i,j+1,m,n) and arr[i][j+1] < min:
		min = arr[i][j+1]
		r = i
		c = j+1
	if isValid(i+1,j,m,n) and arr[i+1][j] < min:
		min = arr[i+1][j]
		r = i+1
		c = j

	return (r,c)
		
					
def isValid(i,j,m,n):
	if i < 0 or j < 0 or i >=m or j >=n:
		return 0
	else:
		return 1
	
def printmat(arr,m,n):
	#print "printing"
	for i in range(m):
		print arr[i]
main()
	
	
