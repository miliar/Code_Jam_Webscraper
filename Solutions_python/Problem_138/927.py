def play_war(nam,ken):
	c = 0
	while(nam):
		chosen_nam = max(nam)
		chosen_ken = max(ken )
		if chosen_nam < chosen_ken:
			chosen_ken = min([k for k in ken if k > chosen_nam])
			
		else:
			chosen_ken = min(ken)
			c+=1
		nam.remove(chosen_nam)
		ken.remove(chosen_ken)

	return c


def play_decwar(nam,ken):
	c = 0
	while(nam):
		if max(nam) < min(ken):
			chosen_nam = min(nam)
			second_max = max(ken)
			if(ken[1:]) : second_max = max(ken[1:])
			told_nam =  second_max + (max(ken) - second_max) / 2
			chosen_ken = max(ken)
			
		#elif max(nam) > max(ken):
		else:		
			told_nam = max(nam) +1
			chosen_ken = min(ken)
			chosen_nam = min([n for n in nam if n > chosen_ken])
			c+=1
		#else:
			#told_nam = max(nam)

		nam.remove(chosen_nam)
		ken.remove(chosen_ken)

	return c

T = input()

for t in range(T):
	N = input()
	nam = sorted([ float(f) for f in raw_input().split(' ') ],reverse = True)
	ken = sorted([ float(f) for f in raw_input().split(' ') ],reverse = True)

	war = play_war(nam[:],ken[:])
	decwar = play_decwar(nam[:],ken[:])
	result = str(decwar) +' '+ str(war)
	print 'Case','#'+str(t+1) + ':', str(result)
