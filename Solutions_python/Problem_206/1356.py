a = int(input())
for  i in range(a):
	b,n = [int(p) for p in raw_input().split(' ')]
	l=[]
	for j in range(n):
		d,s = [int(o) for o in raw_input().split(' ')]
		l.append((b-d)/float(s))
	l.sort(reverse = True)
	sp = b/l[0]
	print 'Case #'+str(i+1)+':',sp