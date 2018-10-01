# deceit to raise value of held block, but still below maximum of ken's chosen one
with open("input.in", 'r') as infile:
	cases = int(infile.readline())
	results = [(0,0)] * cases
	
	for case in range(cases):
		deceit_pt = 0
		normal_pt = 0
		blocks = int(infile.readline())
		
		naomi = infile.readline().split()  # N's blocks
		naomi = [float(x) for x in naomi]
		naomi.sort(reverse = True)  # highest first
		naomi_d = naomi[:]
		
		ken = infile.readline().split()  # K's blocks
		ken = [float(x) for x in ken]
		ken.sort(reverse = True)  # highest first
		ken_d = ken[:]
		
		# deceitful war
		while(len(naomi_d)):
		# when Naomi's lowest is > ken's highest, # of blocks left over is how many pts she get
			temp = naomi_d.pop(0)
			if temp < ken_d.pop(0):  # use lowest to take out ken's highest
				if(len(naomi_d)):
					naomi_d.pop()
					naomi_d.insert(0, temp)
			else:
				deceit_pt += 1

				
		# normal war
		while(len(naomi)):
		# when Naomi's highest < ken's highest, # blocks past is how many pts she get
			temp = ken.pop(0)
			if naomi.pop(0) > temp:
				normal_pt += 1
				if len(ken):
					ken.pop()  # remove last item instead
					ken.insert(0, temp)  # put it back
		
		results[case] = (deceit_pt, normal_pt)
		
	# print out case results
	for case in range(cases):
		print("Case #{}: {} {}".format(case + 1, results[case][0], results[case][1]))