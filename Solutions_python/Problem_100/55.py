import sys

def solve(n,rew):
	print '---------------------------------'	
	s=0
	pts = [0*i for i in range(n)]
	flag = True
	ct = 0

	for i in range(n):
		for j in range(2):
			print rew[i][j],
		print



	while flag:
		ind = -1
		val = -1
		nex = -1
		flag = False
		for i in range(n):
			j = pts[i]
#			print 'before  j is %d'%j
#			print rew[i][j]<=s
#			sys.stdin.readline()	
			modified = False	
			while (j<2 and rew[i][j]<=s):
				j = j + 1
				flag = True
				modified=True
#			print 'i = %d, j = %d'%(i,j)
			if modified and ((j>val) or (j==val and rew[i][j]>nex)):
				ind = i
				val = j
				nex = rew[i][j]

		if flag:
			s = s + val-pts[ind]
			pts[ind] = val 
			ct = ct + 1
#		print '   pinter status'
#		for j in range(n):
#			print pts[j], 
#		print
#		print '  the score = %d'%s
	if s!=n*2: return -1
	else: return ct


if __name__=='__main__':
	
	f = open('B-large.in','r')
	fout = open('B.out','w')


	T = int(f.readline())
	for i in range(T):
		fout.write('Case #%d: '%(i+1))
		n = int(f.readline())
		rew = []
		for i in range(n):
			line = f.readline()
			a = int(line.strip().split()[0])
			b = int(line.strip().split()[1])
			rew.append([a,b,100000000])

		ans = solve(n,rew)
		if ans==-1:
			fout.write('Too Bad\n')
		else:
			fout.write('%d\n'%ans)









	fout.close()
	f.close()	
