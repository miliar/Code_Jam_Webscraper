def dec2bin(n):
	bin = ''
	if n < 0:  raise ValueError, "negatif !"
	if n == 0: return '00000000000000000000'
	i=20 
	while i > 0: #2^20 = 1048576 > 10^6
		i-=1
		bin = str(n % 2) + bin
		n = n >> 1
	return bin

def bin2dec(n):
	dec = 0
	mult=1
	i=20
	while i>0:
		i-=1
		dec += int(n[i]) * mult
		mult*=2
	return dec 

def add(a,b):
	a = dec2bin(a)
	b = dec2bin(b)
	res=''
	for i in xrange(19,-1,-1):
		w=0
		w=int(a[len(a)-i-1])
		w+=int(b[len(b)-i-1])
		w= w%2
		res = res + str(w)
	return bin2dec(res)

def solve(n, l):
	global fin
	somme = 0
	l.sort(reverse=True)
	for i in l:
		somme = add(somme,int(i))
	if somme == 0:
		for i in xrange(n-1):
			somme+=int(l[i])
		return somme
	else:
		return 'NO'

if __name__ == '__main__':
	n = int(raw_input())
	b = [[int(_) for _ in raw_input().split()] for i in xrange(n*2)]	
	for i in xrange(n):
		print 'Case #'+str(i+1)+': '+str(solve(int(b[i*2][0]),b[i*2+1]))

