f = open('a.in')
fo = open('a.out','w')
t = int(f.readline())

for itr in range(t):
	# print('itr = ',itr)
	l = (f.readline()).split()
	smax = int(l[0])
	s = [int(_) for _ in l[1]]
	# print('\tsmax =',smax,'s =',s)

	fr=0
	for i in range(1,smax+1):
		# print('\t\ti =',i,'s['+str(i)+'] =',s[i],'fr =',fr)
		if s[i] != 0:
			if s[i-1] < i:
				fr = fr + i-s[i-1]
				# print('\t\t\tfr =',fr)
				s[i-1] = s[i-1] + i-s[i-1] 
		s[i] = s[i] + s[i-1]

	fo.write('Case #'+str(itr+1)+': '+str(fr)+'\n')

f.close()
fo.close()
###########################