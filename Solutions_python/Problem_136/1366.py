import sys
sys.setrecursionlimit(10000)

def clicker(cost, curr_farm_rate, farm_rate, target, acc_time):
	
	while True:

		time_no_farm = target / curr_farm_rate

		new_farm = cost / curr_farm_rate + target / (curr_farm_rate + farm_rate)

		if time_no_farm > new_farm:
			
			acc_time += cost/curr_farm_rate
			curr_farm_rate += farm_rate
		else:
			return time_no_farm+acc_time
	



def main():
	for case in xrange(1, input()+1):
		c, f, x = map(float, raw_input().split(" "))
		print "Case #%d: %f" % (case, clicker(c,2,f,x,0))

main()