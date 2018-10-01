INITIAL_FREQUENCY = 2 #Eggs/second
COST_INDEX = 0
FREQUENCY_INDEX = 1
GOAL_INDEX = 2

input_file_name = input('Input file name:')
with open(input_file_name) as input_file:
	test_count = int(input_file.readline()) # Get number of tests
	def calc_time(frequency, goal, cookies=0):
		"""Takes the current frequency, the goal and how many cookies we have right now,
		and calculates the time left to solve the problem.
		"""
		missing = goal - cookies
		time = missing / frequency
		return time
	
	def should_buy_farm(frequency, cost, farm_frequency, goal):
		"""Tests if buying a new farm makes the solutiong faster
		than just waiting"""
		
		# The time to buy a new farm, therefore the cost is the goal
		# Plus the time for the goal.
		time_with_farm = calc_time(frequency, cost) +\
							 calc_time(frequency + farm_frequency, goal)
		# Time just waiting
		time_without_farm = calc_time(frequency, goal)
		return time_with_farm < time_without_farm
	with open('output.o', 'w') as output_file:
		for case in range(1, test_count+1):
			# The time to solve this case
			time = 0
			frequency = 2
			data = input_file.readline().split() # Gets data
			cost = float(data[COST_INDEX])
			farm_frequency = float(data[FREQUENCY_INDEX])
			goal = float(data[GOAL_INDEX])
			
			"""The way we solve this, is by continuously buying farms,
			until buying another farm is longer than waiting.
			In this step we assume each time we have 0 cookies to begin with,
			because we either just bought a farm and waiting
			to buy a new one, or bought one and waiting to goal."""
			while should_buy_farm(frequency, cost, farm_frequency, goal):
				# Add the time to buy the new farm, and check again
				time += calc_time(frequency, cost)
				frequency += farm_frequency
			# Add the time for the last part
			time += calc_time(frequency, goal)
			output_file.write('Case #%d: %s\n'%(case, '{0:.7f}'.format(time)))
		