fi = open("B-large.in.txt","r")
fo = open("output","w")
numinst = int(fi.readline())
for k in range(numinst):
	inst = fi.readline().split()
	numact0 = int(inst[0]) 
	numact1 = int(inst[1]) 
	act0 = []
	act1 = []
	for j in range(numact0):
		act = fi.readline().split()
		act0 += [(int(act[0]),int(act[1]),0)]
	for j in range(numact1):
		act = fi.readline().split()
		act1 += [(int(act[0]),int(act[1]),1)]	
	acts = act0+act1
	acts.sort(key=lambda tup: tup[0])
	
	budgets = [720,720]
	switches = 0
	critical_gaps = []
	last_act = acts[len(acts)-1]

	for i in range(len(acts)):
		int_length = 0
		if(acts[i][0] <= acts[i][1]):
			int_length = acts[i][1]-acts[i][0]
		else:
			int_length = acts[i][1]-(acts[i][0]-1440)

		budgets[1-acts[i][2]] -= int_length	
		
		gap_length = 0
		if (last_act[1] <= acts[i][0]):
			gap_length = acts[i][0]-last_act[1]
		else:
			gap_length = acts[i][0]-(last_act[1]-1440)
		
		if (last_act[2] != acts[i][2]):
			switches += 1
		else:
			critical_gaps += [(gap_length,1-last_act[2])]
			
		last_act = acts[i]
		print last_act
		
	critical_gaps.sort(key=lambda tup: tup[0])
	print critical_gaps
	print budgets
	print switches
	for i in range(len(critical_gaps)):
		if(budgets[critical_gaps[i][1]]>=critical_gaps[i][0]):
			budgets[critical_gaps[i][1]]-=critical_gaps[i][0]
		else:
			#budgets[1-critical_gaps[i][1]]-=(critical_gaps[i][0]-budgets[critical_gaps[i][1]])
			#budgets[critical_gaps[i][1]]=0
			switches += 2
	
	fo.write("Case #"+str(k+1)+": "+str(switches)+"\n")
	print k
fo.close()
fi.close()