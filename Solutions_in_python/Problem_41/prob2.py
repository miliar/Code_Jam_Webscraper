'''
Created on Sep 12, 2009
@author: namnx
'''
INFILE = 'prob2-large.in'
OUTFILE = 'prob2-large.out'

def isMax(n):
	l = list(n)
	l = sorted(l)
	l.reverse()
	s = ''.join(l)
	if (s == n):
		return True
	return False
	
def findMaxD(n):
	d = n[0]
	for c in n:
		if c>d: d=c
	return d

def findNextD(d, n):
	l = list(n)
	l = sorted(n)
	i = 0
	while (l[i] <= d): 
		i+=1
	return l[i]
		
def findMinD(n):
	for c in n:
		if c != '0': d = c
	for c in n:
		if c !='0' and c < d:
			d = c
	return d
	
def findMin(n):
	l = list(n)
	l = sorted(l)
	s = ''.join(l)
	return s


def nextnum(n):
	curr = len(n)-2
	while(curr>=0):
		s = n[curr:len(n)]
		if isMax(s): 
			curr -= 1
		else:
			d = findNextD(n[curr], s)
			i = s.index(d)
			s1 = s[0:i] + s[i+1:len(s)]
			s1 = findMin(s1)
			s1 = d + s1
			return n[0:curr] + s1
		
	d = findMinD(n)
	i = n.index(d)
	s = n[0:i] + n[i+1:len(n)]
	s = findMin(s)
	return d + '0' + s


def main():
	fin = file(INFILE, 'r')
	fout = file(OUTFILE, 'w')
	t = int(fin.readline().strip())
	for i in range(t):
		n = fin.readline().strip()
		fout.write('Case #' + str(i+1) + ': ' + nextnum(n) + '\n')
	fin.close()
	fout.close()


if __name__ == '__main__':
	main()
	#print nextnum('80')
