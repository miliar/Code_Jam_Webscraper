import collections
f = open('cookies.in', "r")
lines = f.readlines()
f.close()

cases = int(lines[0])


current_case=1

while current_case < cases+1:
        l = [float(i) for i in lines[current_case].split()]
	C = l[0]
	F = l[1]
	X = l[2]
	
	costs = dict()
	costs[0] = 0
	min_time = X/0.2 
        prev_time = min_time	
	_continue = True
	i = 1

	while _continue:
		current_before_buy = 0.2 + (F*(i-1)/10)
		current_cost = current_before_buy+(F/10)
		costs[i] = costs[i-1] + C/current_before_buy
		time = costs[i] + X/current_cost
		i+=1
		if time < min_time:
			min_time=time
			prev_time = time
		else:
			if time >= prev_time:
				_continue = False
		
		#print time/10 
		#print prev_time/10
		
	
	print "Case #{0}: {1}".format(current_case,min_time/10 )
	current_case+=1	
	
	 
