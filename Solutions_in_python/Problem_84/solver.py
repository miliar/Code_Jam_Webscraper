import sys


def read(R,inIter):
	instance=[]
	for lineNo in range(R):
		line = next(inIter)
		instance.append(list(line.strip()))
	return instance

def draw(instance):
	return '\n'.join(''.join(row) for row in instance)
		
def draw_horizontal(instance):
	C = len(instance)
	if C==0:
		return ''
	R = len(instance[0])
	newInst = []
	for c, col in enumerate(instance):
		for r, cell in enumerate(col):
			if (len(newInst) <= r):
				newInst.append([])
			newInst[r].append(cell)
	return draw(newInst)
	
def solve(R, C, m):
	imp = '\nImpossible'	

	vertical = draw(m)
	if '#' in vertical.replace('##','zz'):
		print "vcheck"
		return imp
		
	horizontal = draw_horizontal(m)
	if '#' in horizontal.replace('##','zz'):
		print "hcheck"
		return imp

	for r,row in enumerate(m):
		top = True
		for c, title in enumerate(row):			
			if (title == '#'):		
				top = r == 0 or m[r-1][c] == '.' or m[r-1][c] == 'b'
				if (not top):
					m[r][c] = 'b'
				else:
					m[r][c] = 't'
	
	result = draw(m).replace('bb', '\\/').replace('tt','/\\')
	if ('b' in result or 't' in  result):
		print "cross check"
		return imp
	
	return '\n'+result
	
fname = sys.argv[1]
inF = open(fname, 'r')
outF = open(fname.replace('.in','')+'.out', 'w')

inIter = iter(inF)
T = int(next(inIter))
for case in range(1, T+1):
	R,C = map(int, next(inIter).split())
	instance = read(R,inIter)
	solution = solve(R, C, instance)
	print >>outF, "Case #%i: %s" % (case, solution)
 

outF.close()