
import sys

def cc(C,F,X, test_case_id):
	# print C,F,X

	current_cookies = 0
	cookies_per_second = 2.0

	saved_times = []
	def sum_time_so_far():
		total = 0.0
		for t in saved_times:
			total = total + t
		return total

	counter = 0
	saved_time_to_win = 0

	while True:
		time_needed_to_win_seconds = X/cookies_per_second
		time_needed_to_make_farm_seconds = C/cookies_per_second
		time_spent_so_far = sum_time_so_far()
		summed_time = time_needed_to_win_seconds - time_needed_to_make_farm_seconds

		# print "time to win:", time_needed_to_win_seconds
		# print "time to make farm:", time_needed_to_make_farm_seconds
		# print "time spent so far:", time_spent_so_far
		# print "time to win + time already taken:", time_needed_to_win_seconds + time_spent_so_far
		saved_time_to_win = time_needed_to_win_seconds + time_spent_so_far
		# print "time to win minus farm build seconds", summed_time
		# print "cookies per second", cookies_per_second
		# print "saved_times", saved_times
		# print "WORK HAPPENED"

		# do all the work for the farm
		saved_times.append(time_needed_to_make_farm_seconds)
		current_cookies = 0
		cookies_per_second = cookies_per_second + F

		time_needed_to_win_seconds = X/cookies_per_second
		time_needed_to_make_farm_seconds = C/cookies_per_second
		time_spent_so_far = sum_time_so_far()
		summed_time = time_needed_to_win_seconds - time_needed_to_make_farm_seconds
		# print "new saved_times", saved_times
		# print "new time to win", time_needed_to_win_seconds
		# print "new time to make farm", time_needed_to_make_farm_seconds
		# print "new total time time_spent_so_far", time_spent_so_far
		# print "new time to win + time already taken:", time_needed_to_win_seconds + time_spent_so_far
		# print "new time to win minus farm build", summed_time
		# print 

		if saved_time_to_win < (time_needed_to_win_seconds+time_spent_so_far):
			print "Case #" + str(test_case_id) + ": " + str(saved_time_to_win)
			break

		counter = counter  + 1

	# print "DONE"
	# print "saved_times", saved_times
	# print "total time spent", sum_time_so_far()

# cc(C,F,X)
# cc(30.0,1.0,2.0)
# cc(30.0,2.0,100.0)
# cc(30.50000,3.14159,1999.19990)

data = open(sys.argv[1],"r").readlines()
current_line = 0
def readline():
	global current_line
	tmp = current_line
	current_line = current_line + 1
	return data[tmp]
test_cases = int(readline())
for i in range(test_cases):
	cfx_data = readline().split()
	cfx_data = map(float, cfx_data)
	# print cfx_data
	cc(cfx_data[0], cfx_data[1], cfx_data[2],i+1)
