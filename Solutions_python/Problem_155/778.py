t = int (raw_input())
p=0
while t:
	t=t-1
	p+=1
	inp = raw_input()
	sm ,ls =inp.split(' ')
	sm=int(sm)
	ls = list(ls)
	#print ls
	people_standing=0
	flag=0
	for shy in range(sm+1):
		current_shy_people=int(ls[shy])
		#print shy,current_shy_people,people_standing
		if shy <= people_standing:
			people_standing+=current_shy_people
		elif current_shy_people:
			#print shy,current_shy_people,people_standing
			temp = shy- people_standing
			people_standing +=temp+current_shy_people
			flag+=temp
			#print'add ',temp
	print 'Case #'+str(p)+': '+str(flag)
