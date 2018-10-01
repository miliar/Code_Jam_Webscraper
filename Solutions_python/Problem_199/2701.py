def allOnes(s):
	for bit in s:
		if bit=='-':
			return False
	return True

def flip(s,i,k):
	r = ""
	for x in range(0,i):
		r = r + s[x]
	for x in range(i,i+k):
		if s[x] =='-':
			r=r+'+'
		else:
			r=r+'-'
	for x in range(i+k,len(s)):
		r = r + s[x]
	return r
				

def solve():
	r = open('input.in','r')
	f = open('output.out','w')	
	#t = int(input())
	t = int(r.readline())
	for j in range(1,t+1):
		#s,k = input().split()
		s,k = str(r.readline()).split()
		k = int(k)
		data = {}
		data[s] = 1
		ans = 0
		while not allOnes(s):
			for i in range(0,len(s)):
				if s[i]=='-' and i+k<=len(s):
					s = flip(s,i,k)
					ans = ans + 1				
			if s in data:
				ans='IMPOSSIBLE'
				break
			else:
				data[s] = 1	
		print('Case #{}: {}'.format(j,ans))
		f.write('Case #{}: {}\n'.format(j,ans))
	r.close()
	f.close()

solve()














