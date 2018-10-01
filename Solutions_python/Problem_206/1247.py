# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	dest, nb_horses = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	dest = dest * 1.000000
	times = []
	for h in range(nb_horses): 
		pos, speed = [int(s) for s in input().split(" ")]
		horse_time = (dest - pos) / speed
		times.append(dest/horse_time)
	print("Case #{}: {}".format(i, min(times)))
	# check out .format's specification for more formatting options
	