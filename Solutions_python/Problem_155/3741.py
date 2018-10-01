import sys

input = file(sys.argv[1]).readline

for i in range(1, int(input()) + 1):
	l, data = input().split(" ")
	sum = 0
	needed = 0 
	for i2 in range(int(l) + 1):
		if sum < i2:
			needed += i2 - sum
			sum = i2
		sum += int(data[i2])
	print "Case #{0}: {1}".format(i, needed)