filename = "C-large.in"
data = [line for line in open(filename).read().split("\n")][0:-1]

data = [[int(x) for x in line.split(" ")] for line in data]

t = data[0][0]
data = data[1:]


for x in xrange(0, len(data), 2):
	num_rides, capacity, num_groups = data[x]
	groups = data[x+1]

	starting_index = 0

	total_so_far = 0
	dp = {}
	rides_so_far = 0
	use_dp = True

	while True:
		if use_dp and starting_index in dp:
			dp_table = dp[starting_index]
			num_rides_loop = rides_so_far - dp_table["num_rides"]
			money_loop = total_so_far - dp_table["total_money"]
			remaining_rides = num_rides - rides_so_far
			num_times_repeated = remaining_rides/num_rides_loop
			
			total_so_far += money_loop * num_times_repeated
			rides_so_far += num_rides_loop * num_times_repeated

			use_dp = False

		if rides_so_far == num_rides:
			break

		dp[starting_index] = {
			"num_rides": rides_so_far,
			"total_money": total_so_far,
		}
		index = starting_index
		this_ride = 0
		while this_ride + groups[index] <= capacity:
			this_ride += groups[index]
			index = (index + 1) % num_groups
			if index == starting_index:
				break
		rides_so_far += 1
		total_so_far += this_ride
		starting_index = index
		#print rides_so_far, total_so_far, starting_index

	print "Case #%d: %d" % (x/2+1, total_so_far)





