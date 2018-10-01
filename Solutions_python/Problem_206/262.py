t = int(input())
for t_i in range(t):
	d, n = map(int, input().split())
	max_time = 0
	for n_i in range(n):
		ki, si = map(int, input().split())
		time_to_arrival = (d-ki)/si
		max_time = max(max_time, time_to_arrival)
	print("Case #%d: %.6f" % (t_i+1, d/max_time))
	