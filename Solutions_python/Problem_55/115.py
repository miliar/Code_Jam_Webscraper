t = int(raw_input())
for i in xrange(1,t+1):
	R, k, N = map(int,raw_input().split())
	g = map(int,raw_input().split())
	time_reached = N*[0]
	j = 0
	t = 1
	n_people = []
	while time_reached[j%N] == 0:
		prev_j = j
		time_reached[j%N] = t
		t+=1
		n_people.append(0)
		while n_people[-1]+g[j%N] <= k:
			n_people[-1] += g[j%N]
			j+=1
			if prev_j%N == j%N: break
	cycle_start = time_reached[j%N]-1
	cycle_len = t-time_reached[j%N]
	for k in xrange(cycle_start,cycle_start+cycle_len):
		n_people.append(n_people[k])
	sum_people = [0]
	for k in n_people:
		sum_people.append(k)
		if len(sum_people) > 1:
			sum_people[-1] += sum_people[-2]
	euros = 0
	euros += sum_people[min(cycle_start, R)]
	euros += (max(0,(R-cycle_start)/cycle_len))*(sum_people[cycle_start+cycle_len] - sum_people[cycle_start])
	euros += sum_people[cycle_start+max(0,(R-cycle_start))%cycle_len] - sum_people[cycle_start]
	print "Case #%d: %d" % (i,euros)
