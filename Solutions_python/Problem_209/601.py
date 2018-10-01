import sys
import operator
import math

f = open(sys.argv[1], 'r')
g = open(sys.argv[2], 'w')

lines = f.readlines()

f.close()

N = int(lines[0])

i = 1

for n in range(1, N+1):
	print "case n: " + str(n)
	print lines[i]
	a = int(lines[i].split()[0])
	q = int(lines[i].split()[1])
	pancakes = []
	for p in range(1, a+1):
		radius = int(lines[i+p].split()[0])
		height = int(lines[i+p].split()[1])
		pancakes += [[radius, height, 2*math.pi*radius*height+math.pi*radius*radius, 2*math.pi*radius*height]]
	#brute force
	sorted_pancakes = sorted(pancakes, reverse = True)
	max_base = 0
	base_radius = 0
	base_index = -1
	max_ans = -1
	for p in range(0, a-q+1):
		print "p: " + str(p) 
		filtered_pancakes = sorted(sorted_pancakes[p+1:], key=lambda x: (x[3]), reverse=True)
		extra = sum([x[3] for x in filtered_pancakes[:q-1]])
		ans = extra + sorted_pancakes[p][2]
		if ans > max_ans:
			max_ans = ans
	g.write("Case #" + str(n) + ": " + str(max_ans).replace("+", "") + "\n")
	print "Case #" + str(n) + ": " + str(max_ans)
	i += a+1

g.close()


