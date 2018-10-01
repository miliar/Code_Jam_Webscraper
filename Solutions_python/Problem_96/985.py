T = int(raw_input().strip())

for i in xrange(T):
	print 'Case #%s:' %(i+1),
	score_list = []
	elements = raw_input().strip().split()
	N, S, p = int(elements[0]), int(elements[1]), int(elements[2])
	score_list = [int(score) for score in elements[3:]]
	max_possible = 0
	for score in score_list:
		max_score = 0
		if score == 0 and p > 0:
			continue
		avg_score = int(score/3)
		remainder = int(score%3)
		
		if (avg_score >= p):
			max_possible = max_possible + 1
		else:		
			if ((avg_score + 2) < p ):
				# no way to reach to p
				max_score = avg_score	
			elif ((avg_score + 1) >= p):
				# difference is only 1 from avg_score
				if (remainder > 0):
					# either remainder can be adjusted 
					max_score = avg_score + 1
				elif (S>0):
					S = S - 1
					max_score = avg_score + 1
				else:
					max_score = avg_score
			elif ((avg_score+2) >=  p):
				if (S>0) and (remainder == 2):
					S = S - 1
					max_score = avg_score + 2
				elif (S > 0) and (remainder == 1):
					max_score = avg_score + 1
				else:
					max_score = avg_score + 1
			else:
				max_score = avg_score
			#print avg_score	, remainder, S, max_score, max_possible	
			if (max_score >= p):
				max_possible = max_possible + 1
		#print max_possible
	print max_possible
