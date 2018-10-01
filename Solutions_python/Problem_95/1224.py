def execute():
	sol = {'a': 'y','b': 'h','c': 'e','d': 's','e': 'o',
	'f': 'c','g': 'v','h': 'x','i': 'd','j': 'u','k': 'i','l': 'g',
	'm': 'l','n': 'b','o': 'k','p': 'r','q': 'z','r': 't','s': 'n',
	't': 'w','u': 'j','v': 'p','w': 'f','x': 'm','y': 'a','z': 'q',' ':' '}
	filename = 'A-small-attempt0.in'
	fp = open(filename,"r")
	noc = int(fp.readline())
	for x in range(noc):
		ans=[]
		line = fp.readline().strip()
		for i in line:
			ans.append(sol[i])
		print 'Case #%d:'%(x+1),
		print ''.join(ans)
		
if __name__=='__main__':
	execute()