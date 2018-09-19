import sys 

if len(sys.argv) > 1: 
	f = open(sys.argv[1])
	a = f.read()
	f.close()
else:
	a = '''4
5
1 2 3 4 5
3
3 5 6
7
3 4 5 6 7 8 11
15
505941 453285 557971 384221 834522 159409 450338 762932 606094 905873 288679 357891 304741 132239 851346'''

b = a.split('\n')

def check(n,k):
	temp = 0
	for i in range(n):
		temp = temp ^ int(k[i])
	if temp == 0:
		s = 0
		k.sort(key=float)
		for j in range(n-1):
			s = s + int(k[j+1])
		return s	
	else:
		return False



#if sys.argv[2]:
#	w = file(sys.argv[2], 'a')
#else:
#	w = file(test4.out, 'a')
w = file('test4.out', 'a')
for i in range(int(b[0])):
	e = b[(i+1)*2].split(' ')
	c = check(int(b[i*2+1]),e)
	if c:
		w.write('Case #%d: %d\n' % ((i+1),c))
	else:
		w.write('Case #%d: NO\n' % (i+1))
w.close()
