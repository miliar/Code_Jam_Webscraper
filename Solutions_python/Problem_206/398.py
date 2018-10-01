import os
import sys
import decimal

num_tests = 0
num_horses = 0
distance = 0
horses = []
decimal.getcontext().prec=100
def solve():
	d = [None]*len(horses)
	d[0] = (distance - horses[0][0])/decimal.Decimal(horses[0][1])
	prev_speed = horses[0][1]
	prev_start = horses[0][0]
	prev_total_time = 0
#	print "AAAAAAAAAAAA"
	for i in xrange(1, len(horses)):
		start, speed = horses[i]
		speed_diff = speed - prev_speed
		start_diff = prev_start - start

		prev_start = start
		if speed_diff <= 0:
#			print i, "slower"
			prev_speed = speed
			d[i] = (distance - start)/decimal.Decimal(speed)
		elif (start_diff / decimal.Decimal(speed_diff)) > (distance - start) / decimal.Decimal(speed):
#			print i, "wont meet"
			prev_speed = speed
			d[i] = (distance - start)/decimal.Decimal(speed)
		else:
#			print i, "faster"
			time_to_catch_up = (start_diff / decimal.Decimal(speed_diff))
#			print time_to_catch_up
#			print (distance - time_to_catch_up*float(speed) - start)/prev_speed
			total_time = time_to_catch_up + (distance - time_to_catch_up*decimal.Decimal(speed) - start)/prev_speed
			d[i] = total_time
			prev_speed = distance / total_time

		#print 'ps', prev_speed

	#print horses, d

	return "%.7f" % (float(distance / d[len(horses) - 1]),)

def process_line(l, i):
	global num_tests,num_horses,distance,horses
	if i == 0:
		num_tests = int(i)
	elif num_horses == 0:
		distance,num_horses = [int(a) for a in l.split()]
	else:
		horses.append([int(a) for a in l.split()])
		if len(horses) == num_horses:
			r = solve()
			horses = []
			num_horses = 0
			return r

def main():

	fn = sys.argv[1]
	fn_out = sys.argv[2]
	lines = open(fn, 'rb').read().splitlines()
	out_fd = open(fn_out, 'wb')
	i = 0
	case_num = 0
	for line in lines:
		s = process_line(line, i)
		i += 1
		if s is not None:
			case_num += 1
			out_fd.write('Case #%d: %s' % (case_num, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()