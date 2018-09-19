tc = int(raw_input())


def isPossible(n,c,d):
	#print "checkin for ",n
	if n in d:
		return True;
	else:
		d = sorted(d)[::-1]
		cc = c
		i=0

		while n > 0 and i < len(d):
			#print "n",n,cc,i,d[i]
			if n - d[i] > -1 and cc > 0:
				n -= d[i]
				cc-=1
			else:
				i+=1

			if cc == 0:
				i+=1
				cc=c
		#print "after n",n
		if n == 0:
			return True
		else:
			return False






for i in range(tc):
	c,d,v = map(int, raw_input().split(' '))
	d_a = map(int, raw_input().split(' '))

	ans = 0
	for j in range(1,v+1):

		if not isPossible(j,c,d_a):
			ans+=1;
			d_a.append(j)

	print "Case #"+str((i+1))+":",ans
